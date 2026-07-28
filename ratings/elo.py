"""
Project Gridiron
Elo Rating System

Version 0.1
"""

DEFAULT_ELO = 1500


def expected_score(team_a, team_b):
    return 1 / (1 + 10 ** ((team_b - team_a) / 400))


def update_elo(team_rating, opponent_rating, result, k=20):

    expected = expected_score(team_rating, opponent_rating)

    return round(
        team_rating + k * (result - expected),
        2
    )


if __name__ == "__main__":

    chiefs = DEFAULT_ELO
    bills = DEFAULT_ELO

    chiefs = update_elo(chiefs, bills, 1)
    bills = update_elo(bills, chiefs, 0)

    print("Chiefs:", chiefs)
    print("Bills:", bills)
