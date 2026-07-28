"""
Project Gridiron
Matchup Predictor

Version 2.0
"""

from models.rating_storage import load_ratings


HOME_FIELD = 50


def predict_matchup(home_team, away_team):

    ratings = load_ratings()

    home_rating = ratings[home_team] + HOME_FIELD
    away_rating = ratings[away_team]

    difference = home_rating - away_rating

    win_probability = 50 + (difference / 10)

    if win_probability > 95:
        win_probability = 95

    if win_probability < 5:
        win_probability = 5

    winner = (
        home_team
        if difference > 0
        else away_team
    )

    return {
        "winner": winner,
        "win_probability": round(win_probability, 1),
        "rating_difference": round(difference, 1)
    }


if __name__ == "__main__":

    prediction = predict_matchup(
        "Kansas City Chiefs",
        "Buffalo Bills"
    )

    print("🏈 PROJECT GRIDIRON MATCHUP")
    print(prediction)
