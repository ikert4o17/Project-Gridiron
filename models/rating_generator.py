"""
Project Gridiron
Rating Generator

Version 0.1
"""

from data.team_metrics import nfl_metrics
from ratings.stat_converter import (
    offense_rating,
    defense_rating,
    overall_rating
)


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

    print(f"\n{team['name']}")
    print(f"Offense Rating: {offense}")
    print(f"Defense Rating: {defense}")
    print(f"Overall Rating: {overall}")
