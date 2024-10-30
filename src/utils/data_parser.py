# utils/data_parser.py

import csv
import os
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import PatternFill

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


def save_to_csv(results, filepath="test-output/csv-summary/test_report.csv"):
    """
    Saves the results to a CSV file for easy viewing and analysis.

    :param results: List of dictionaries with request results.
    :param filepath: File path for the CSV file.
    """
    # Create a DataFrame from results
    df = pd.DataFrame(results)

    # Replace boolean values with Yes/No for better readability
    df['success'] = df['success'].replace({True: 'Yes', False: 'No'})

    # Save DataFrame to a CSV file
    df.to_csv(filepath, index=False)

    print(f"CSV report saved successfully at: {filepath}")

    # Optionally, if you want to save it in Excel with formatting
    save_to_excel(results)


def save_to_excel(results, filepath="test-output/excel-report/test_report.xlsx"):
    """
    Saves the results to an Excel file with color formatting for better visualization.

    :param results: List of dictionaries with request results.
    :param filepath: File path for the Excel file.
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Create a DataFrame from results
    df = pd.DataFrame(results)

    # Replace boolean values with Yes/No for better readability
    df['success'] = df['success'].replace({True: 'Yes', False: 'No'})

    # Create an Excel writer object
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        # Write the DataFrame to the Excel file
        df.to_excel(writer, index=False, sheet_name='Test Results')

        # Access the workbook and the active worksheet
        workbook = writer.book
        worksheet = writer.sheets['Test Results']

        # Define colors for success and failure
        success_fill = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')  # Light green
        failure_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')  # Light red

        # Print unique values to debug
        print(df['success'].unique())  # Debugging line to check success values

        # Apply color formatting based on success
        for row in worksheet.iter_rows(min_row=2, max_col=len(df.columns)):  # Loop through all columns
            success_value = row[2].value  # Get value of the 'success' column (4th column)
            if success_value == 'Yes':
                for cell in row:
                    cell.fill = success_fill
            elif success_value == 'No':
                for cell in row:
                    cell.fill = failure_fill

    print(f"Excel report saved successfully at: {filepath}")