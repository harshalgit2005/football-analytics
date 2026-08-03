
import json
from pathlib import Path

import pandas as pd


# File Paths


RAW_FILE = Path("data/raw/matches.json")

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "matches.csv"


# Load JSON


print("=" * 60)
print("LOADING MATCH DATA")
print("=" * 60)

with open(RAW_FILE, "r", encoding="utf-8") as file:
    matches = json.load(file)

df = pd.json_normalize(matches)

print(f"Original Records : {len(df)}")
print(f"Original Columns : {len(df.columns)}")


# Keep Required Columns


required_columns = [

    "id",

    "utcDate",

    "status",

    "matchday",

    "stage",

    "competition.id",
    "competition.name",

    "season.id",

    "homeTeam.id",
    "homeTeam.name",

    "awayTeam.id",
    "awayTeam.name",

    "score.winner",

    "score.fullTime.home",
    "score.fullTime.away"
]

existing_columns = [
    col
    for col in required_columns
    if col in df.columns
]

df = df[existing_columns]

print(f"Columns Retained : {len(existing_columns)}")


# Remove Duplicate Matches


duplicates = df.duplicated(subset="id").sum()

df.drop_duplicates(
    subset="id",
    inplace=True
)

print(f"Duplicate Matches Removed : {duplicates}")


# Convert UTC Date


df["utcDate"] = pd.to_datetime(
    df["utcDate"],
    utc=True,
    errors="coerce"
)

invalid_dates = df["utcDate"].isna().sum()

df.dropna(
    subset=["utcDate"],
    inplace=True
)

print(f"Invalid Dates Removed : {invalid_dates}")


# Split Datetime


df["date"] = df["utcDate"].dt.date

df["time"] = df["utcDate"].dt.time

df["year"] = df["utcDate"].dt.year

df["month"] = df["utcDate"].dt.month

df["month_name"] = df["utcDate"].dt.month_name()

df["day"] = df["utcDate"].dt.day

df["weekday"] = df["utcDate"].dt.day_name()

df["week"] = df["utcDate"].dt.isocalendar().week.astype(int)

df["hour"] = df["utcDate"].dt.hour


# Handle Missing Scores

df["score.fullTime.home"] = (
    df["score.fullTime.home"]
    .fillna(-1)
    .astype(int)
)

df["score.fullTime.away"] = (
    df["score.fullTime.away"]
    .fillna(-1)
    .astype(int)
)

missing_scores = (
    (df["score.fullTime.home"] == -1)
    |
    (df["score.fullTime.away"] == -1)
).sum()

print(f"Matches Without Final Score : {missing_scores}")


# Remove Rows with Missing Teams


before = len(df)

df.dropna(
    subset=[
        "homeTeam.id",
        "awayTeam.id"
    ],
    inplace=True
)

after = len(df)

print(f"Rows Removed (Missing Teams): {before - after}")


# Rename Columns


df.rename(
    columns={
        "id": "match_id",

        "utcDate": "match_datetime",

        "competition.id": "competition_id",
        "competition.name": "competition",

        "season.id": "season_id",

        "homeTeam.id": "home_team_id",
        "homeTeam.name": "home_team",

        "awayTeam.id": "away_team_id",
        "awayTeam.name": "away_team",

        "score.winner": "winner",

        "score.fullTime.home": "home_score",
        "score.fullTime.away": "away_score"
    },
    inplace=True
)


# Reorder Columns


column_order = [

    "match_id",

    "competition_id",
    "competition",

    "season_id",

    "match_datetime",

    "date",
    "time",

    "year",
    "month",
    "month_name",

    "day",
    "weekday",
    "week",

    "hour",

    "matchday",

    "stage",

    "status",

    "home_team_id",
    "home_team",

    "away_team_id",
    "away_team",

    "home_score",
    "away_score",

    "winner"
]

df = df[[col for col in column_order if col in df.columns]]


# Final Sort


df.sort_values(
    by="match_datetime",
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


print("\n" + "=" * 60)
print("MATCH CLEANING COMPLETED")
print("=" * 60)

print(f"Final Records : {len(df)}")
print(f"Final Columns : {len(df.columns)}")
print(f"Saved File    : {OUTPUT_FILE}")

print("=" * 60)

print("\nPreview:\n")
print(df.head())