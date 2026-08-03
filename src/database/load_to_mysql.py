
from pathlib import Path

import pandas as pd

from db_connection import get_engine


# Paths


DATA_FOLDER = Path("data/processed")

MATCHES = DATA_FOLDER / "matches.csv"
TEAMS = DATA_FOLDER / "teams.csv"
STANDINGS = DATA_FOLDER / "standings.csv"

engine = get_engine()


# Load Matches


print("=" * 60)
print("Loading Matches")
print("=" * 60)

matches = pd.read_csv(
    MATCHES
)

matches.to_sql(
    "matches",
    con=engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(matches)} matches")


# Load Teams


print("=" * 60)
print("Loading Teams")
print("=" * 60)

teams = pd.read_csv(
    TEAMS
)

teams.to_sql(
    "teams",
    con=engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(teams)} teams")


# Load Standings


print("=" * 60)
print("Loading Standings")
print("=" * 60)

standings = pd.read_csv(
    STANDINGS
)

standings.to_sql(
    "standings",
    con=engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(standings)} standings")

print("\n")

print("=" * 60)
print("ALL TABLES LOADED SUCCESSFULLY")
print("=" * 60)