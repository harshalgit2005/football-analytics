
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

# Output folder
RAW_FOLDER = Path("data/raw")
RAW_FOLDER.mkdir(parents=True, exist_ok=True)


def save_json(data, filepath):
    """Save JSON data to a file."""
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def fetch_standings():
    """Fetch standings from all selected competitions."""

    all_standings = []

    print("=" * 60)
    print("Downloading League Standings")
    print("=" * 60)

    for league, code in COMPETITIONS.items():

        print(f"\nFetching standings for {league}...")

        data = get_data(f"/competitions/{code}/standings")

        if data is None:
            print(f"Failed to fetch {league}")
            continue

        standings = data.get("standings", [])

        # Add league name to each standings group
        for standing in standings:
            standing["competition"] = league
            standing["competition_code"] = code

        all_standings.extend(standings)

        print(f"Downloaded {len(standings)} standing table(s)")

    output_file = RAW_FOLDER / "standings.json"

    save_json(all_standings, output_file)

    print("\n" + "=" * 60)
    print(f"Standing Groups : {len(all_standings)}")
    print(f"Saved To        : {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    fetch_standings()