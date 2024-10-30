# utils/data_parser.py

import csv

def filter_results(results, success=True):
    """
    Filters the test results to include only successful or failed requests.
    :param results: List of dictionaries with request results.
    :param success: Boolean to filter success (True) or failed (False) requests.
    :return: Filtered list of request results.
    """
    return [result for result in results if result["success"] == success]

def extract_response_times(results):
    """
    Extracts response times from the results for analysis.
    :param results: List of dictionaries with request results.
    :return: List of response times (float).
    """
    return [result["response_time"] for result in results if result["response_time"] is not None]

def calculate_percentile(response_times, percentile):
    """
    Calculates a specific percentile for response times (e.g., 90th percentile).
    :param response_times: List of response times.
    :param percentile: Percentile to calculate (e.g., 90 for 90th percentile).
    :return: Calculated percentile value.
    """
    if not response_times:
        return None
    sorted_times = sorted(response_times)
    index = int(len(sorted_times) * (percentile / 100))
    return sorted_times[index]

def save_to_csv(results, filepath="test-output/csv-report/test_report.csv"):
    """
    Saves the results to a CSV file for easy viewing and analysis.
    :param results: List of dictionaries with request results.
    :param filepath: File path for the CSV file.
    """
    keys = results[0].keys() if results else []
    with open(filepath, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
