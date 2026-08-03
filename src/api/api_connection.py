

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base URL for Football-Data API
BASE_URL = "https://api.football-data.org/v4"

# Read API Key
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError(
        "API_KEY not found. Please add it to your .env file."
    )

# Authentication headers
HEADERS = {
    "X-Auth-Token": API_KEY,
    "Accept": "application/json"
}


def get_data(endpoint: str, params: dict = None):
    """
    Fetch data from Football-Data API.

    Parameters
    ----------
    endpoint : str
        API endpoint (e.g. '/competitions')
    params : dict, optional
        Query parameters

    Returns
    -------
    dict
        JSON response
    """

    url = f"{BASE_URL}{endpoint}"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(response.text)
        return None

    except requests.exceptions.ConnectionError:
        print("Connection Error. Check your internet.")
        return None

    except requests.exceptions.Timeout:
        print("Request Timed Out.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Unexpected Error: {e}")
        return None


def test_connection():
    """
    Test API connection using the competitions endpoint.
    """

    print("Testing Football-Data API...")

    data = get_data("/competitions")

    if data is None:
        print("Connection Failed")
        return False

    print("Connection Successful")
    print(f"Competitions Found: {len(data['competitions'])}")

    return True


if __name__ == "__main__":
    test_connection()