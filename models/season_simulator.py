"""
Project Gridiron
Season Simulator

Version 0.1
"""

from ratings.elo import DEFAULT_ELO, update_elo

teams = {
    "Kansas City Chiefs": DEFAULT_ELO,
    "Buffalo Bills": DEFAULT_ELO,
    "Philadelphia Eagles": DEFAULT_ELO,
    "Dallas Cowboys": DEFAULT_ELO
}

games = [
    ("Kansas City Chiefs", "Buffalo Bills", "Kansas City Chiefs"),
    ("Philadelphia Eagles", "Dallas Cowboys", "Philadelphia Eagles"),
]

for home, away, winner in games:

    home_rating = teams[home]
    away_rating = teams[away]

    if winner == home:
        home_new = update_elo(home_rating, away_rating, 1)
        away_new = update_elo(away_rating, home_rating, 0)
    else:
        home_new = update_elo(home_rating, away_rating, 0)
        away_new = update_elo(away_rating, home_rating, 1)

    teams[home] = home_new
    teams[away] = away_new

print("Updated Elo Ratings\n")

for team, rating in sorted(
    teams.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{team}: {rating}")
