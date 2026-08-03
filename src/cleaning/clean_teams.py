

import json
from pathlib import Path

import pandas as pd


# File Paths


RAW_FILE = Path("data/raw/teams.json")

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "teams.csv"


# Load JSON


print("=" * 60)
print("LOADING TEAM DATA")
print("=" * 60)

with open(RAW_FILE, "r", encoding="utf-8") as file:
    teams = json.load(file)

df = pd.json_normalize(teams)

print(f"Original Records : {len(df)}")
print(f"Original Columns : {len(df.columns)}")


# Keep Required Columns


required_columns = [

    "id",

    "name",

    "shortName",

    "tla",

    "founded",

    "venue",

    "clubColors",

    "website",

    "address",

    "area.id",

    "area.name",

    "area.code",

    "coach.id",

    "coach.name",

    "coach.nationality",

    "coach.dateOfBirth",

    "crest"
]

existing_columns = [
    col
    for col in required_columns
    if col in df.columns
]

df = df[existing_columns]

print(f"Columns Retained : {len(existing_columns)}")


# Remove Duplicate Teams


duplicates = df.duplicated(subset="id").sum()

df.drop_duplicates(
    subset="id",
    inplace=True
)

print(f"Duplicate Teams Removed : {duplicates}")


# Handle Missing Values


df["venue"] = df["venue"].fillna("Unknown Venue")

df["website"] = df["website"].fillna("")

df["clubColors"] = df["clubColors"].fillna("Unknown")

df["coach.name"] = df["coach.name"].fillna("Unknown")

df["coach.nationality"] = df["coach.nationality"].fillna("Unknown")

df["coach.dateOfBirth"] = pd.to_datetime(
    df["coach.dateOfBirth"],
    errors="coerce"
)

df["founded"] = (
    df["founded"]
    .fillna(0)
    .astype(int)
)


# Rename Columns


df.rename(
    columns={

        "id": "team_id",

        "name": "team_name",

        "shortName": "short_name",

        "tla": "team_code",

        "founded": "founded_year",

        "venue": "stadium",

        "clubColors": "club_colors",

        "website": "website",

        "address": "address",

        "area.id": "country_id",

        "area.name": "country",

        "area.code": "country_code",

        "coach.id": "coach_id",

        "coach.name": "coach_name",

        "coach.nationality": "coach_nationality",

        "coach.dateOfBirth": "coach_birth_date",

        "crest": "crest_url"

    },
    inplace=True
)


# Reorder Columns


column_order = [

    "team_id",

    "team_name",

    "short_name",

    "team_code",

    "country_id",

    "country",

    "country_code",

    "founded_year",

    "stadium",

    "club_colors",

    "website",

    "address",

    "coach_id",

    "coach_name",

    "coach_nationality",

    "coach_birth_date",

    "crest_url"
]

df = df[[col for col in column_order if col in df.columns]]


# Sort Teams


df.sort_values(
    by="team_name",
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
print("TEAM CLEANING COMPLETED")
print("=" * 60)

print(f"Final Records : {len(df)}")
print(f"Final Columns : {len(df.columns)}")
print(f"Saved File    : {OUTPUT_FILE}")

print("=" * 60)

print("\nPreview:\n")
print(df.head())