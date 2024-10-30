# core/metrics.py

def calculate_metrics(results):
    """
    Calculates performance metrics from the request results.

    :param results: List of dictionaries with request results.
    :return: A dictionary containing average, minimum, and maximum response times.
    """
    # Extract response times, filtering out None values
    response_times = [result['response_time'] for result in results if 'response_time' in result and result['response_time'] is not None]

    # Calculate metrics, ensuring we handle cases with no valid response times
    if not response_times:
        return {
            "average_response_time": None,
            "min_response_time": None,
            "max_response_time": None,
            "error": "No valid response times available."
        }

    average_response_time = sum(response_times) / len(response_times)
    min_response_time = min(response_times)
    max_response_time = max(response_times)

    return {
        "average_response_time": average_response_time,
        "min_response_time": min_response_time,
        "max_response_time": max_response_time,
        # Add other metrics as needed
    }
