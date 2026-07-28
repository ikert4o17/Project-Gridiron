"""
Project Gridiron
Ranking Movement Tracker

Version 1.0
"""

import json

from models.rating_storage import load_ratings


CURRENT_FILE = "storage/ratings.json"
PREVIOUS_FILE = "storage/previous_rankings.json"


def get_rankings():

    ratings = load_ratings()

    return [
        team for team, rating in sorted(
            ratings.items(),
            key=lambda x: x[1],
            reverse=True
        )
    ]


def save_previous(rankings):

    with open(PREVIOUS_FILE, "w") as file:
        json.dump(rankings, file, indent=4)


current = get_rankings()

print("🏈 PROJECT GRIDIRON MOVEMENT\n")

for index, team in enumerate(current, start=1):
    print(f"{index}. {team}")


save_previous(current)
