from concurrent.futures import ThreadPoolExecutor

from config.config import TIMEOUT, BASE_URL
from core.metrics import calculate_metrics
from core.report_generator import generate_report
from core.request_handler import fetch_url


def load_test_with_increasing_concurrency(start_users=1, max_users=20, step=5, requests_per_level=10):
    all_results = {}
    all_metrics = {}

    for concurrent_users in range(start_users, max_users + 1, step):
        print(f"[INFO] Testing with {concurrent_users} concurrent users...")

        results = []
        with ThreadPoolExecutor(max_workers=concurrent_users) as executor:
            futures = [executor.submit(fetch_url, BASE_URL, TIMEOUT) for _ in range(requests_per_level)]
            for future in futures:
                results.append(future.result())

        # Calculate metrics for this concurrency level
        metrics = calculate_metrics(results)
        all_results[concurrent_users] = results
        all_metrics[concurrent_users] = metrics

        print(f"[INFO] Metrics for {concurrent_users} users: {metrics}")

    # Generate a unified report for all load levels
    generate_report(all_results, all_metrics, filepath="test-output/json-summary/unified_report.json")
    print("[INFO] Load test completed. Unified report generated.")
