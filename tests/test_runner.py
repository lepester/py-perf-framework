# tests/test_runner.py

from concurrent.futures import ThreadPoolExecutor
from src.config.config import BASE_URL, NUM_REQUESTS, CONCURRENT_USERS, TIMEOUT
from src.core.request_handler import fetch_url
from src.core.metrics import calculate_metrics
from src.core.report_generator import generate_report, create_output_directories
from src.utils.logger import setup_logger
from src.utils.data_parser import extract_response_times, calculate_percentile, save_to_csv, generate_visualizations, \
    save_to_excel

logger = setup_logger()

def run_test():
    """
    Runs performance tests against the specified URL with concurrent requests,
    generates reports for analysis, and handles any errors during execution.

    This function uses a thread pool to send requests concurrently, analyzes
    the results, and generates reports even if some requests fail.
    """
    results = []
    with ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:
        futures = [executor.submit(fetch_url, BASE_URL, TIMEOUT) for _ in range(NUM_REQUESTS)]
        for future in futures:
            results.append(future.result())

    # Filter only failed requests for debugging or error analysis
    failed_requests = [result for result in results if not result["success"]]
    logger.info(f"Number of Failed Requests: {len(failed_requests)}")

    # Check if all requests failed
    if len(failed_requests) == NUM_REQUESTS:
        logger.error("All requests have failed. The website might be down.")
        metrics = {
            "average_response_time": None,
            "min_response_time": None,
            "max_response_time": None,
            "error": "All requests failed. Website might be down."
        }
    else:
        # Extract response times and calculate the 90th percentile
        response_times = extract_response_times(results)
        ninety_percentile_time = calculate_percentile(response_times, 90) if response_times else None

        if ninety_percentile_time is None:
            logger.warning("90th Percentile Response Time: N/A (No valid response times available)")
        else:
            logger.info(f"90th Percentile Response Time: {ninety_percentile_time:.2f} seconds")

        # Calculate metrics
        metrics = calculate_metrics(results)

    # Generate both CSV and JSON reports
    try:
        save_to_csv(results, filepath="test-output/csv-summary/test_report.csv")
        generate_report(results, metrics, filepath="test-output/json-summary/test_summary.json")
    except Exception as e:
        logger.error(f"Error generating reports: {e}")

    # Generate Excel and visualization reports
    try:
        save_to_excel(results, filepath="test-output/excel-report/test_report.xlsx")
        generate_visualizations(results)
    except Exception as e:
        logger.error(f"Error generating Excel or visualizations: {e}")

    logger.info("Test run finished. Reports generated at test-output/excel-report and test-output/visualizations")
