"""
Project Gridiron
Team Rating Engine

Version 0.2
"""

from data.teams import nfl_teams, college_teams


def calculate_rating(team):
    rating = (
        team["offense"] * 0.4 +
        team["defense"] * 0.4
    )

    return round(rating, 2)


print("NFL Rankings")
print("----------------")

for team in nfl_teams:
    rating = calculate_rating(team)
    print(team["name"], rating)


print("\nCollege Football Rankings")
print("----------------")

for team in college_teams:
    rating = calculate_rating(team)
    print(team["name"], rating)
