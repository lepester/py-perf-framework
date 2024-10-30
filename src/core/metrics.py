# core/metrics.py

def calculate_metrics(results):
    response_times = [result['response_time'] for result in results if 'response_time' in result]

    # Calculate metrics
    average_response_time = sum(response_times) / len(response_times) if response_times else 0
    min_response_time = min(response_times) if response_times else 0
    max_response_time = max(response_times) if response_times else 0

    return {
        "average_response_time": average_response_time,
        "min_response_time": min_response_time,
        "max_response_time": max_response_time,
        # Add other metrics as needed
    }
