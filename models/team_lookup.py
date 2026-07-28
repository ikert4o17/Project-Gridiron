"""
Project Gridiron
Team Lookup

Version 1.0
"""

from data.nfl_ratings import nfl_ratings


def get_team_rating(team_name):

    rating = nfl_ratings.get(team_name)

    if rating is None:
        return f"{team_name} was not found."

    return {
        "team": team_name,
        "elo": rating
    }


if __name__ == "__main__":

    print(get_team_rating("Kansas City Chiefs"))
    print(get_team_rating("Philadelphia Eagles"))
