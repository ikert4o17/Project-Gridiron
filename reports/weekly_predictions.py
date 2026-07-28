"""
Project Gridiron
Weekly Prediction Report

Version 1.0
"""

from data.games import nfl_week
from predictions.matchup_predictor import predict_matchup


print("🏈 PROJECT GRIDIRON WEEKLY PREDICTIONS\n")


for game in nfl_week:

    prediction = predict_matchup(
        game["home"],
        game["away"]
    )

    print("--------------------------------")
    print(f"{game['away']} @ {game['home']}")
    print(f"Pick: {prediction['winner']}")
    print(
        f"Win Probability: "
        f"{prediction['win_probability']}%"
    )
    print(
        f"Rating Difference: "
        f"{prediction['rating_difference']}"
    )
