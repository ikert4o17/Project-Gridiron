"""
Project Gridiron
Weekly Power Rankings

Version 1.0
"""

from models.rating_storage import load_ratings


def generate_rankings():

    ratings = load_ratings()

    rankings = sorted(
        ratings.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return rankings


print("🏈 PROJECT GRIDIRON POWER RANKINGS\n")

rankings = generate_rankings()

for position, (team, rating) in enumerate(
    rankings,
    start=1
):
    print(
        f"{position}. {team} - {rating}"
    )
