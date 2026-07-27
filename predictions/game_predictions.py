"""
Project Gridiron
Game Prediction Engine

Version 0.1
"""

from ratings.team_ratings import calculate_rating


def predict_game(home_team, away_team):

    home_rating = calculate_rating(home_team)
    away_rating = calculate_rating(away_team)

    difference = home_rating - away_rating

    if difference > 0:
        winner = home_team["name"]
    else:
        winner = away_team["name"]

    return {
        "winner": winner,
        "margin": round(abs(difference), 2)
    }


example_home = {
    "name": "Kansas City Chiefs",
    "offense": 90,
    "defense": 85
}

example_away = {
    "name": "Buffalo Bills",
    "offense": 87,
    "defense": 86
}


prediction = predict_game(example_home, example_away)

print(prediction)
