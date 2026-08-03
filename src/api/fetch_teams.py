

import json
from pathlib import Path

from api_connection import get_data

# Competitions to fetch
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


def fetch_teams():
    """Fetch teams from all selected competitions."""

    all_teams = {}
    total_downloaded = 0

    print("=" * 60)
    print("Downloading Teams")
    print("=" * 60)

    for league, code in COMPETITIONS.items():

        print(f"\nFetching teams from {league}...")

        data = get_data(f"/competitions/{code}/teams")

        if data is None:
            print(f"Failed to fetch {league}")
            continue

        teams = data.get("teams", [])

        print(f"Found {len(teams)} teams")

        total_downloaded += len(teams)

        # Remove duplicates using team id
        for team in teams:
            all_teams[team["id"]] = team

    unique_teams = list(all_teams.values())

    output_file = RAW_FOLDER / "teams.json"

    save_json(unique_teams, output_file)

    print("\n" + "=" * 60)
    print(f"Downloaded : {total_downloaded}")
    print(f"Unique Teams: {len(unique_teams)}")
    print(f"Saved to    : {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    fetch_teams()