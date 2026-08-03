"""
Downloads all matches from selected competitions
and saves them as data/raw/matches.json
"""

import json
from pathlib import Path

from api_connection import get_data

# Competition codes
COMPETITIONS = {
    "Premier League": "PL",
    "La Liga": "PD",
    "Champions League": "CL",
    "Bundesliga": "BL1",
    "Serie A": "SA"
}

# Output directory
RAW_FOLDER = Path("data/raw")
RAW_FOLDER.mkdir(parents=True, exist_ok=True)


def save_json(data, filepath):
    """Save JSON data to a file."""
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def fetch_matches():
    """Fetch matches from all selected competitions."""

    all_matches = {}
    total_downloaded = 0

    print("=" * 60)
    print("Downloading Matches")
    print("=" * 60)

    for league, code in COMPETITIONS.items():

        print(f"\nFetching matches from {league}...")

        data = get_data(f"/competitions/{code}/matches")

        if data is None:
            print(f"Failed to fetch {league}")
            continue

        matches = data.get("matches", [])

        print(f"Found {len(matches)} matches")

        total_downloaded += len(matches)

        # Remove duplicates using match ID
        for match in matches:
            all_matches[match["id"]] = match

    unique_matches = list(all_matches.values())

    output_file = RAW_FOLDER / "matches.json"

    save_json(unique_matches, output_file)

    print("\n" + "=" * 60)
    print(f"Downloaded Matches : {total_downloaded}")
    print(f"Unique Matches     : {len(unique_matches)}")
    print(f"Saved To           : {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    fetch_matches()