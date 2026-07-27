"""
Project Gridiron
Game Prediction Engine

Version 0.2
"""

from ratings.team_ratings import calculate_rating
from ratings.adjustments import apply_home_field


def predict_game(home_team, away_team):

    home_rating = calculate_rating(home_team)
    away_rating = calculate_rating(away_team)

    home_rating = apply_home_field(home_rating, True)

    margin = home_rating - away_rating

    if margin > 0:
        winner = home_team["name"]
    else:
        winner = away_team["name"]

    confidence = min(abs(margin) * 10, 95)

    return {
        "winner": winner,
        "projected_margin": round(margin, 2),
        "confidence": round(confidence, 1)
    }


home_team = {
    "name": "Kansas City Chiefs",
    "offense": 90,
    "defense": 85,
    "strength_of_schedule": 82
}

away_team = {
    "name": "Buffalo Bills",
    "offense": 87,
    "defense": 86,
    "strength_of_schedule": 84
}


prediction = predict_game(home_team, away_team)

print(prediction)
