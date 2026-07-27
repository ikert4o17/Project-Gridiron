"""
Project Gridiron
Team Rating Engine

Version 0.1
"""

teams = {
    "Example Team": {
        "offense": 85,
        "defense": 80,
        "strength_of_schedule": 75
    }
}


def calculate_rating(team):
    rating = (
        team["offense"] * 0.4 +
        team["defense"] * 0.4 +
        team["strength_of_schedule"] * 0.2
    )

    return round(rating, 2)


for name, stats in teams.items():
    print(name, calculate_rating(stats))
