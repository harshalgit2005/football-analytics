"""
Downloads competition data from Football-Data.org API
and saves each response as a JSON file.

"""

import json
from pathlib import Path

from api_connection import get_data

# Competition codes used by Football-Data.org
COMPETITIONS = {
    "Premier_League": "PL",
    "La_Liga": "PD",
    "Champions_League": "CL",
    "Bundesliga": "BL1",
    "Serie_A": "SA"
}

# Create data/raw folder if it doesn't exist
RAW_FOLDER = Path("data/raw")
RAW_FOLDER.mkdir(parents=True, exist_ok=True)


def save_json(data, filepath):
    """Save JSON data to a file."""
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def fetch_competitions():
    """Fetch and save competition details."""

    print("=" * 60)
    print("Downloading Competition Data")
    print("=" * 60)

    for league_name, code in COMPETITIONS.items():

        print(f"\nFetching {league_name}...")

        data = get_data(f"/competitions/{code}")

        if data is None:
            print(f"Failed to fetch {league_name}")
            continue

        filename = RAW_FOLDER / f"{league_name.lower()}.json"

        save_json(data, filename)

        print(f"Saved: {filename}")


if __name__ == "__main__":
    fetch_competitions()