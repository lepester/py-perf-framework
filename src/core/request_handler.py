# core/request_handler.py

import requests
import time

def fetch_url(url, timeout):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        elapsed_time = time.time() - start_time
        return {
            "status_code": response.status_code,
            "response_time": elapsed_time,
            "success": response.ok
        }
    except requests.RequestException as e:
        return {
            "status_code": None,
            "response_time": None,
            "success": False,
            "error": str(e)
        }
