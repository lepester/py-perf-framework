# main.py
from src.core.report_generator import create_output_directories
from tests.test_runner import run_tests
from tests.load_test_runner import load_test_with_increasing_concurrency

if __name__ == "__main__":
    # Generate test-output directories
    create_output_directories()
    # Run the standard test suite
    run_tests()

    # Run load test with increasing concurrency
    load_test_with_increasing_concurrency(start_users=1, max_users=20, step=5, requests_per_level=10)
