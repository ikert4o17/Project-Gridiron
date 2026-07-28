"""
Project Gridiron
Power Rankings

Version 0.1
"""

from data.team_metrics import nfl_metrics
from ratings.stat_converter import (
    offense_rating,
    defense_rating,
    overall_rating
)

rankings = []

for team in nfl_metrics:

    offense = offense_rating(
        team["points_per_game"],
        team["yards_per_play"]
    )

    defense = defense_rating(
        team["points_allowed"]
    )

    overall = overall_rating(
        offense,
        defense
    )

    rankings.append({
        "team": team["name"],
        "rating": overall
    })

rankings.sort(
    key=lambda x: x["rating"],
    reverse=True
)

print("🏈 Project Gridiron NFL Power Rankings\n")

for i, team in enumerate(rankings, start=1):
    print(f"{i}. {team['team']} - {team['rating']}")
