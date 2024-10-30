# main.py
from src.core.report_generator import create_output_directories
from tests.test_runner import run_test

if __name__ == "__main__":
    # Generate test-output directories
    create_output_directories()

    # Run the standard test suite
    run_test()
