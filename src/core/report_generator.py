# core/report_generator.py

import json
import os

def create_output_directories():
    # Define the main output directory and subdirectories
    main_dir = 'test-output'
    csv_dir = os.path.join(main_dir, 'csv-report')
    json_dir = os.path.join(main_dir, 'json-summary')

    # Check if the main directory exists
    if os.path.exists(main_dir):
        return

    # Create the main directory and subdirectories
    os.makedirs(csv_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

def generate_report(all_results, all_metrics, filepath="../json-summary/unified_report.json"):
    """
    Generates a unified report of the test results.
    :param all_results: Dictionary containing all results grouped by test and concurrency level.
    :param all_metrics: Dictionary containing all performance metrics grouped by test and concurrency level.
    :param filepath: Path to save the report.
    """
    # Prepare report data
    report_data = {
        "results": all_results,
        "metrics": all_metrics
    }

    # Save report as JSON
    with open(filepath, "w") as f:
        json.dump(report_data, f, indent=4)
