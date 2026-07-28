"""
Project Gridiron
Elo Rating Updater

Version 1.1
"""

from data.results import nfl_results
from models.rating_storage import (
    load_ratings,
    save_ratings
)
from ratings.elo import update_elo


def update_ratings():

    nfl_ratings = load_ratings()

    for game in nfl_results:

        winner = game["winner"]
        loser = game["loser"]

        winner_rating = nfl_ratings[winner]
        loser_rating = nfl_ratings[loser]

        new_winner_rating = update_elo(
            winner_rating,
            loser_rating,
            1
        )

        new_loser_rating = update_elo(
            loser_rating,
            winner_rating,
            0
        )

        nfl_ratings[winner] = new_winner_rating
        nfl_ratings[loser] = new_loser_rating


    save_ratings(nfl_ratings)

    return nfl_ratings


updated = update_ratings()


print("🏈 Ratings Updated\n")

for team, rating in sorted(
    updated.items(),
    key=lambda x: x[1],
    reverse=True
):

    print(f"{team}: {rating}")
