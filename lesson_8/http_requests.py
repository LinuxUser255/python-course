#!/usr/bin/env python3
import requests
from requests.exceptions import RequestException

BASIC_URL = "https://jsonplaceholder.typicode.com/posts/1"

def fetch_post(url: str = BASIC_URL) -> dict | None:
    try:
        response = requests.get(url, timeout=10) #  GET request method
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Request failed: {e}")
        return None

print(fetch_post())
