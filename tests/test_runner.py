# tests/test_runner.py

from concurrent.futures import ThreadPoolExecutor
from src.config.config import BASE_URL, NUM_REQUESTS, CONCURRENT_USERS, TIMEOUT
from src.core.request_handler import fetch_url
from src.core.metrics import calculate_metrics
from src.core.report_generator import generate_report, create_output_directories
from src.utils.data_parser import extract_response_times, calculate_percentile, save_to_csv


def run_tests():
    # Generate test-output directories
    create_output_directories()

    results = []
    with ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:
        futures = [executor.submit(fetch_url, BASE_URL, TIMEOUT) for _ in range(NUM_REQUESTS)]
        for future in futures:
            results.append(future.result())

    # Filter only failed requests for debugging or error analysis
    failed_requests = [result for result in results if not result["success"]]
    print(f"Number of Failed Requests: {len(failed_requests)}")

    # Check if all requests failed
    if len(failed_requests) == NUM_REQUESTS:
        print("All requests have failed. The website might be down.")
        # Log failure in metrics report
        metrics = {
            "average_response_time": None,
            "min_response_time": None,
            "max_response_time": None,
            "error": "All requests failed. Website might be down."
        }
        # Save an empty or informative CSV report
        save_to_csv(results, filepath="test-output/csv-summary/test_report.csv")
        generate_report(results, metrics, filepath="test-output/json-summary/test_summary.json")
        return

    # Extract response times and calculate the 90th percentile
    response_times = extract_response_times(results)
    ninety_percentile_time = calculate_percentile(response_times, 90) if response_times else None

    if ninety_percentile_time is None:
        print("90th Percentile Response Time: N/A (No valid response times available)")
    else:
        print(f"90th Percentile Response Time: {ninety_percentile_time:.2f} seconds")

    # Calculate metrics and save detailed CSV report
    metrics = calculate_metrics(results)
    save_to_csv(results, filepath="test-output/csv-summary/test_report.csv")

    # Generate the report correctly
    generate_report(results, metrics, filepath="test-output/json-summary/test_summary.json")

    print("Test completed. Report and CSV file generated.")
