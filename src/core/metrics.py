# core/metrics.py

def calculate_metrics(results):
    """
    Calculates performance metrics from the request results.

    :param results: List of dictionaries with request results.
    :return: A dictionary containing average, minimum, and maximum response times.
    """
    # Extract response times, filtering out None values and ensuring valid keys are present
    response_times = [
        result['response_time'] for result in results
        if 'response_time' in result and result['response_time'] is not None
    ]

    # Calculate metrics, ensuring we handle cases with no valid response times
    if not response_times:
        return {
            "average_response_time": None,  # No average response time available
            "min_response_time": None,       # No minimum response time available
            "max_response_time": None,       # No maximum response time available
            "error": "No valid response times available."  # Error message for clarity
        }

    # Calculate average, minimum, and maximum response times
    average_response_time = sum(response_times) / len(response_times)  # Average calculation
    min_response_time = min(response_times)  # Minimum response time
    max_response_time = max(response_times)  # Maximum response time

    return {
        "average_response_time": average_response_time,  # Returning calculated average
        "min_response_time": min_response_time,           # Returning calculated minimum
        "max_response_time": max_response_time,           # Returning calculated maximum
        # Add other metrics as needed
    }
