def elo_win_probability(home_rating, away_rating):

    return 1 / (
        1 + 10 ** ((away_rating - home_rating) / 400)
    )
