from concurrent.futures import ThreadPoolExecutor
from src.config.config import TIMEOUT, BASE_URL
from src.core.metrics import calculate_metrics
from src.core.report_generator import generate_report
from src.core.request_handler import fetch_url

def load_test_with_increasing_concurrency(start_users=1, max_users=20, step=5, requests_per_level=10):
    """
    Conducts a load test by gradually increasing the number of concurrent users.

    :param start_users: The initial number of concurrent users to start the test with.
    :param max_users: The maximum number of concurrent users for the test.
    :param step: The increment step for increasing concurrent users.
    :param requests_per_level: The number of requests to send at each concurrency level.
    """
    all_results = {}  # Dictionary to store results for each level of concurrency
    all_metrics = {}  # Dictionary to store metrics for each level of concurrency

    # Loop through the range of concurrent users, increasing by the specified step
    for concurrent_users in range(start_users, max_users + 1, step):
        print(f"[INFO] Testing with {concurrent_users} concurrent users...")

        results = []  # List to collect results for the current concurrency level
        with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            # Submit requests to be executed concurrently
            futures = [executor.submit(fetch_url, BASE_URL, TIMEOUT) for _ in range(requests_per_level)]
            for future in futures:
                results.append(future.result())  # Collect the result of each request

        # Calculate performance metrics for the current level of concurrency
        metrics = calculate_metrics(results)
        all_results[concurrent_users] = results  # Store the results for this concurrency level
        all_metrics[concurrent_users] = metrics  # Store the metrics for this concurrency level

        print(f"[INFO] Metrics for {concurrent_users} users: {metrics}")

    # Generate a unified report that summarizes results and metrics for all load levels
    generate_report(all_results, all_metrics, filepath="test-output/json-summary/unified_report.json")
    print("[INFO] Load test completed. Unified report generated.")
