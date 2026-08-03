

import numpy as np
import pandas as pd

from src.database.db_connection import get_engine


# Connect to MySQL


engine = get_engine()


# Load Tables


matches = pd.read_sql(
    "SELECT * FROM matches",
    engine
)

standings = pd.read_sql(
    "SELECT * FROM standings",
    engine
)


# Goal Difference


matches["goal_difference"] = (
    matches["home_score"] -
    matches["away_score"]
)


# Total Goals


matches["total_goals"] = (
    matches["home_score"] +
    matches["away_score"]
)


# Match Result


matches["result"] = np.where(

    matches["home_score"] >
    matches["away_score"],

    "Home Win",

    np.where(

        matches["home_score"] <
        matches["away_score"],

        "Away Win",

        "Draw"

    )

)


# Home Win Flag


matches["home_win"] = np.where(
    matches["winner"] == "HOME_TEAM",
    1,
    0
)


# Away Win Flag


matches["away_win"] = np.where(
    matches["winner"] == "AWAY_TEAM",
    1,
    0
)


# Draw Flag


matches["draw"] = np.where(
    matches["winner"] == "DRAW",
    1,
    0
)


# Goals Per Match


standings["goals_per_match"] = (
    standings["goals_for"] /
    standings["played_games"]
).round(2)


# Win Percentage


standings["win_percentage"] = (
    standings["won"] /
    standings["played_games"] * 100
).round(2)


# Draw Percentage


standings["draw_percentage"] = (
    standings["draw"] /
    standings["played_games"] * 100
).round(2)


# Loss Percentage


standings["loss_percentage"] = (
    standings["lost"] /
    standings["played_games"] * 100
).round(2)


# Clean Sheets Estimate


standings["clean_sheet_rate"] = (
    (
        standings["played_games"] -
        standings["goals_against"]
    )
    .clip(lower=0)
    /
    standings["played_games"]
).round(2)


# Team Strength Score


standings["team_strength_score"] = (

    standings["points"] * 0.5 +

    standings["goal_difference"] * 0.3 +

    standings["won"] * 0.2

).round(2)


# Recent Form Score


form_map = {
    "W": 3,
    "D": 1,
    "L": 0
}

def calculate_form_score(form):

    if pd.isna(form):
        return 0

    score = 0

    for letter in str(form):

        score += form_map.get(letter, 0)

    return score

standings["recent_form_score"] = (
    standings["form"]
    .apply(calculate_form_score)
)


# Save Back to MySQL


matches.to_sql(
    "matches",
    con=engine,
    if_exists="replace",
    index=False
)

standings.to_sql(
    "standings",
    con=engine,
    if_exists="replace",
    index=False
)

print("=" * 60)
print("FEATURE ENGINEERING COMPLETED")
print("=" * 60)

print("Matches Shape :", matches.shape)
print("Standings Shape :", standings.shape)

print("=" * 60)