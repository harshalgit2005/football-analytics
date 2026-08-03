"""
Generate exploratory data analysis charts
from MySQL data.

"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from src.database.db_connection import get_engine


# Connecting to Database


engine = get_engine()


# Creating Images Folder


IMAGE_DIR = Path("images")
IMAGE_DIR.mkdir(exist_ok=True)


# Load Data


matches = pd.read_sql("SELECT * FROM matches", engine)
standings = pd.read_sql("SELECT * FROM standings", engine)

matches["match_datetime"] = pd.to_datetime(matches["match_datetime"])


# Goal Distribution


plt.figure(figsize=(10, 6))

plt.hist(
    matches["total_goals"],
    bins=12
)

plt.title("Goal Distribution")

plt.xlabel("Goals")

plt.ylabel("Matches")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "goal_distribution.png",
    dpi=300
)

plt.close()


# Home vs Away Wins


wins = [
    matches["home_win"].sum(),
    matches["away_win"].sum(),
    matches["draw"].sum()
]

labels = [
    "Home",
    "Away",
    "Draw"
]

plt.figure(figsize=(7, 7))

plt.pie(
    wins,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Home vs Away Wins")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "home_vs_away_wins.png",
    dpi=300
)

plt.close()


# Monthly Goals


monthly = (
    matches
    .groupby("month_name")["total_goals"]
    .sum()
)

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly = monthly.reindex(month_order).dropna()

plt.figure(figsize=(12,6))

plt.plot(
    monthly.index,
    monthly.values,
    marker="o"
)

plt.xticks(rotation=45)

plt.title("Monthly Goals")

plt.xlabel("Month")

plt.ylabel("Goals")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "monthly_goals.png",
    dpi=300
)

plt.close()

# League Comparison


league = (
    matches
    .groupby("competition")["total_goals"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10,6))

plt.barh(
    league.index,
    league.values
)

plt.title("Average Goals per League")

plt.xlabel("Average Goals")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "league_comparison.png",
    dpi=300
)

plt.close()

# Top Scoring Teams


top_attack = (
    standings
    .sort_values("goals_for", ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

plt.barh(
    top_attack["team_name"],
    top_attack["goals_for"]
)

plt.title("Top Scoring Teams")

plt.xlabel("Goals")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "top_scoring_teams.png",
    dpi=300
)

plt.close()


# Top Defensive Teams


top_defense = (
    standings
    .sort_values("goals_against")
    .head(10)
)

plt.figure(figsize=(10,6))

plt.barh(
    top_defense["team_name"],
    top_defense["goals_against"]
)

plt.title("Top Defensive Teams")

plt.xlabel("Goals Conceded")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "top_defensive_teams.png",
    dpi=300
)

plt.close()


# Correlation Heatmap


numeric = standings[[
    "played_games",
    "won",
    "draw",
    "lost",
    "points",
    "goals_for",
    "goals_against",
    "goal_difference",
    "team_strength_score"
]]

corr = numeric.corr()

plt.figure(figsize=(10,8))

plt.imshow(
    corr,
    aspect="auto"
)

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=90
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.colorbar()

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    IMAGE_DIR / "correlation_heatmap.png",
    dpi=300
)

plt.close()


# Report


print("=" * 60)
print("EDA COMPLETED")
print("=" * 60)

print(f"Charts saved to: {IMAGE_DIR.resolve()}")

for file in sorted(IMAGE_DIR.glob("*.png")):
    print(file.name)

print("=" * 60)