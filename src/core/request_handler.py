# core/request_handler.py

import requests
import time

def fetch_url(url, timeout):
    """
    Fetches a URL and measures the response time.

    :param url: The URL to fetch.
    :param timeout: The maximum time to wait for a response (in seconds).
    :return: A dictionary containing status code, response time, success status, and error message if any.
    """
    start_time = time.time()  # Record the start time of the request
    try:
        # Make a GET request to the specified URL with the given timeout
        response = requests.get(url, timeout=timeout)
        elapsed_time = time.time() - start_time  # Calculate the elapsed time for the request

        return {
            "status_code": response.status_code,  # HTTP status code of the response
            "response_time": elapsed_time,         # Time taken to receive the response
            "success": response.ok                  # Boolean indicating if the request was successful
        }
    except requests.RequestException as e:
        # Handle any request exceptions and return error details
        return {
            "status_code": None,                    # No status code available due to failure
            "response_time": None,                  # No response time available due to failure
            "success": False,                        # Indicate the request was not successful
            "error": str(e)                         # Error message from the exception
        }
