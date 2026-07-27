"""
Project Gridiron
Weekly Prediction Runner

Version 0.1
"""

from data.games import nfl_week
from data.teams import nfl_teams
from ratings.team_ratings import calculate_rating
from ratings.adjustments import apply_home_field


def find_team(name):
    for team in nfl_teams:
        if team["name"] == name:
            return team

    return None


def predict_game(home_name, away_name):

    home_team = find_team(home_name)
    away_team = find_team(away_name)

    if home_team is None or away_team is None:
        return "Team data missing"

    home_rating = calculate_rating(home_team)
    away_rating = calculate_rating(away_team)

    home_rating = apply_home_field(home_rating, True)

    margin = home_rating - away_rating

    winner = home_name if margin > 0 else away_name

    return {
        "matchup": f"{home_name} vs {away_name}",
        "winner": winner,
        "margin": round(abs(margin), 2)
    }


for game in nfl_week:

    prediction = predict_game(
        game["home"],
        game["away"]
    )

    print(prediction)
