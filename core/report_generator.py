# core/report_generator.py

import json

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
