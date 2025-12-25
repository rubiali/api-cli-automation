import requests

def fetch_users(api_url: str):
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()
    return response.json()
