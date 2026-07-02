import requests


def fetch_headers(url: str) -> dict:
    try:
        response = requests.get(url, timeout=5)
        return dict(response.headers)

    except requests.exceptions.RequestException:
        return {}
