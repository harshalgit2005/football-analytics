# ⚽ Football Performance Analytics

### Which teams consistently outperform the league, and what performance metrics contribute most to their success?

**Answer:** Built an end-to-end football analytics platform using live data from the Football-Data.org API to identify performance trends, measure team efficiency, and uncover the factors contributing to league success through SQL, Python, MySQL, and Power BI.

---

# Project Overview

Football clubs generate thousands of match events every season, making it difficult to manually evaluate team performance and identify meaningful trends.

In this project, I worked as a **Data Analyst** supporting a football analytics department. The objective was to build an automated analytics pipeline that collects live football data, stores it in a relational database, transforms it into business-ready datasets, and delivers interactive dashboards to support tactical and performance analysis.

The project demonstrates a complete data analytics workflow from API ingestion to executive reporting.

---

# Business Problem

A football club's sporting director wants to answer questions such as:

- Which teams consistently outperform the league?
- How significant is home advantage?
- Which teams have the strongest attack and defense?
- What factors contribute most to league position?
- Which performance metrics should be monitored throughout the season?

Instead of relying on static reports, this project creates a centralized analytics platform using live football data.

---

# Project Architecture

```
Football-Data API
        │
        ▼
Python Requests
        │
        ▼
Raw JSON Files
        │
        ▼
Pandas Data Cleaning
        │
        ▼
MySQL Database
        │
        ▼
SQL Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Recommendations
```

---

# Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Collection | Requests API |
| Data Cleaning | Pandas, NumPy |
| Database | MySQL |
| SQL | MySQL Queries, Joins, CTEs, Window Functions |
| Visualization | Power BI |
| Version Control | Git & GitHub |

---

# Data Source

**API**

Football-Data.org

The API provides live football data including:

- Premier League
- La Liga
- Champions League
- Bundesliga
- Serie A
- League Standings
- Match Results
- Teams
- Competitions

---

# Dataset Information

| Attribute | Value |
|------------|-------|
| Source | Football-Data.org API |
| Format | JSON |
| Refresh | Live API |
| Storage | MySQL |
| Grain | One row per football match |
| Analysis Level | Team & Match |
| Dashboard | Power BI |

---

# Data Schema

## Matches

| Column | Description |
|----------|-------------|
| match_id | Match Identifier |
| competition | Competition |
| utc_date | Match Date |
| home_team | Home Team |
| away_team | Away Team |
| home_score | Home Goals |
| away_score | Away Goals |
| winner | Match Winner |

---

## Teams

| Column | Description |
|----------|-------------|
| team_id | Team ID |
| team_name | Team Name |
| venue | Stadium |
| founded | Founded Year |

---

## League Standings

| Column | Description |
|----------|-------------|
| position | League Position |
| team | Team Name |
| played | Matches Played |
| won | Wins |
| draw | Draws |
| lost | Losses |
| goals_for | Goals Scored |
| goals_against | Goals Conceded |
| goal_difference | Goal Difference |
| points | League Points |

---

# Methodology

## 1. Data Collection

- Connected to the Football-Data.org REST API.
- Retrieved competitions, teams, matches, and league standings.
- Stored raw JSON responses for traceability.

---

## 2. Data Storage

- Loaded raw datasets into MySQL.
- Maintained separate raw and processed datasets.

---

## 3. Data Cleaning

Using Pandas:

- Removed duplicate records
- Standardized team names
- Converted UTC timestamps
- Fixed missing values
- Removed unnecessary columns
- Corrected data types

---

## 4. Feature Engineering

Created business KPIs including:

- Goal Difference
- Home Win Percentage
- Away Win Percentage
- Average Goals per Match
- Points per Match
- Team Strength Score

---

## 5. SQL Analytics

Performed analytical SQL using:

- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING
- Common Table Expressions (CTEs)
- Window Functions
- Aggregate Functions

---

## 6. Dashboard Development

Connected Power BI directly to MySQL and created four interactive dashboards.

---

# Dashboard 1 — Match Result Distribution

<p align="center">
<img src="images/match result distribution.png" width="100%">
</p>

This dashboard summarizes overall match outcomes, goal distribution, and home vs. away performance, providing an overview of league-wide trends.

---

# Dashboard 2 — Top 10 Teams by Points

<p align="center">
<img src="images/top 10 teams by points.png" width="100%">
</p>

This dashboard highlights the highest-performing clubs based on league points, enabling quick comparison of the strongest teams in the competition.

---

# Dashboard 3 — Team Analysis

<p align="center">
<img src="images/team analysis.png" width="100%">
</p>

Provides detailed team-level performance metrics including goals scored, goals conceded, wins, losses, draws, and overall efficiency.

---

# Dashboard 4 — League Analysis

<p align="center">
<img src="images/league analysis.png" width="100%">
</p>

Compares league-wide statistics, identifies scoring trends, and evaluates competitive balance across teams.

---

# Key Findings

After analyzing live football data, the following insights were identified:

- Home teams consistently performed better than away teams, indicating a measurable home advantage.
- Teams with a positive goal difference generally finished higher in the league standings.
- Higher defensive efficiency (fewer goals conceded) showed a stronger relationship with league position than simply scoring more goals.
- The top-performing clubs maintained more consistent results throughout the season compared to lower-ranked teams.
- League standings were heavily influenced by goal difference in closely contested positions.

---

# Business Recommendations

| Recommendation | Owner | Expected Outcome |
|---------------|-------|------------------|
| Improve away-match tactical preparation | Coaching Staff | Increase away win percentage |
| Prioritize defensive improvements for teams conceding above league average | Coaching Staff | Reduce goals conceded |
| Benchmark high-performing clubs to identify successful tactical patterns | Performance Analysis Team | Improve team consistency |
| Monitor goal difference and points per match as primary KPIs | Sporting Director | Better performance tracking |

---

# Limitations & Assumptions

- API coverage depends on the Football-Data.org free plan.
- Historical data availability varies between competitions.
- Player-level performance metrics are limited on the free tier.
- External factors such as injuries, transfers, and tactical changes are not included.
- Results are based only on the competitions and seasons analyzed.

---

# Repository Structure

```
football-performance-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│   └── football_analytics.pbix
│
├── images/
│   ├── match result distribution.png
│   ├── top 10 teams by points.png
│   ├── team analysis.png
│   └── league analysis.png
│
├── notebooks/
│
├── sql/
│
├── src/
│   ├── api/
│   ├── analysis/
│   ├── cleaning/
│   ├── database/
│   ├── features/
│   └── utils/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# How to Reproduce

1. Clone this repository.

```bash
git clone https://github.com/yourusername/football-performance-analytics.git
```

2. Create a virtual environment.

```bash
python -m venv .venv
```

3. Activate the environment.

```bash
.venv\Scripts\activate
```

4. Install dependencies.

```bash
pip install -r requirements.txt
```

5. Create a `.env` file.

```
FOOTBALL_API_KEY=YOUR_API_KEY

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=football_analytics
```

6. Run the API ingestion scripts.

7. Load cleaned data into MySQL.

8. Open `football_analytics.pbix`.

9. Refresh the Power BI dashboard.

---

# Future Improvements

- Automate daily API refresh using GitHub Actions.
- Add player-level performance analytics.
- Include expected goals (xG) and expected assists (xA) metrics.
- Build predictive models for match outcome forecasting.
- Deploy an interactive web dashboard using Streamlit.

---

# Author

**Harshal Saudagar**

Aspiring Data Analyst | Python | SQL | MySQL | Power BI | Data Visualization | ETL | Business Intelligence

If you found this project useful, consider giving the repository a ⭐.