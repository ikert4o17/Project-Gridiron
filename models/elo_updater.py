"""
Project Gridiron
Elo Rating Updater

Version 1.0
"""

from data.nfl_ratings import nfl_ratings
from data.results import nfl_results
from ratings.elo import update_elo


def update_ratings():

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


    return nfl_ratings


updated_ratings = update_ratings()


print("🏈 Updated NFL Elo Ratings\n")

for team, rating in sorted(
    updated_ratings.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]:

    print(f"{team}: {rating}")
