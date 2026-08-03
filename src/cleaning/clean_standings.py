

import json
from pathlib import Path

import pandas as pd


# File Paths


RAW_FILE = Path("data/raw/standings.json")

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "standings.csv"


# Load JSON


print("=" * 60)
print("LOADING STANDINGS DATA")
print("=" * 60)

with open(RAW_FILE, "r", encoding="utf-8") as file:
    standings = json.load(file)

rows = []

# Flatten JSON


for standing in standings:

    competition = standing.get("competition", "")
    competition_code = standing.get("competition_code", "")

    stage = standing.get("stage", "")
    standing_type = standing.get("type", "")

    for team in standing.get("table", []):

        rows.append({

            "competition": competition,
            "competition_code": competition_code,

            "stage": stage,
            "standing_type": standing_type,

            "position": team.get("position"),

            "team_id": team.get("team", {}).get("id"),
            "team_name": team.get("team", {}).get("name"),
            "team_short_name": team.get("team", {}).get("shortName"),
            "team_tla": team.get("team", {}).get("tla"),

            "played_games": team.get("playedGames"),

            "won": team.get("won"),
            "draw": team.get("draw"),
            "lost": team.get("lost"),

            "points": team.get("points"),

            "goals_for": team.get("goalsFor"),
            "goals_against": team.get("goalsAgainst"),

            "goal_difference": team.get("goalDifference"),

            "form": team.get("form")
        })

df = pd.DataFrame(rows)

print(f"Original Records : {len(df)}")
print(f"Original Columns : {len(df.columns)}")


# Remove Duplicate Records


duplicates = df.duplicated(
    subset=["competition", "team_id"]
).sum()

df.drop_duplicates(
    subset=["competition", "team_id"],
    inplace=True
)

print(f"Duplicate Records Removed : {duplicates}")


# Handle Missing Values


numeric_columns = [
    "position",
    "played_games",
    "won",
    "draw",
    "lost",
    "points",
    "goals_for",
    "goals_against",
    "goal_difference"
]

for column in numeric_columns:
    df[column] = (
        df[column]
        .fillna(0)
        .astype(int)
    )

text_columns = [
    "competition",
    "competition_code",
    "stage",
    "standing_type",
    "team_name",
    "team_short_name",
    "team_tla",
    "form"
]

for column in text_columns:
    df[column] = df[column].fillna("Unknown")


# Rename Columns


df.rename(
    columns={
        "competition": "league",
        "competition_code": "league_code",
        "standing_type": "table_type"
    },
    inplace=True
)


# Reorder Columns


column_order = [

    "league",

    "league_code",

    "stage",

    "table_type",

    "position",

    "team_id",

    "team_name",

    "team_short_name",

    "team_tla",

    "played_games",

    "won",

    "draw",

    "lost",

    "points",

    "goals_for",

    "goals_against",

    "goal_difference",

    "form"

]

df = df[[col for col in column_order if col in df.columns]]


# Sort Data


df.sort_values(
    by=["league", "position"],
    inplace=True
)

df.reset_index(
    drop=True,
    inplace=True
)


# Save CSV


df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)


# Report
# 

print("\n" + "=" * 60)
print("STANDINGS CLEANING COMPLETED")
print("=" * 60)

print(f"Final Records : {len(df)}")
print(f"Final Columns : {len(df.columns)}")
print(f"Saved File    : {OUTPUT_FILE}")

print("=" * 60)

print("\nPreview:\n")
print(df.head())