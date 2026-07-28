"""
Project Gridiron
Rating Storage Manager

Version 1.0
"""

import json


FILE = "storage/ratings.json"


def load_ratings():

    with open(FILE, "r") as file:
        return json.load(file)


def save_ratings(ratings):

    with open(FILE, "w") as file:
        json.dump(
            ratings,
            file,
            indent=4
        )


if __name__ == "__main__":

    ratings = load_ratings()

    print("Current Project Gridiron Ratings\n")

    for team, rating in ratings.items():
        print(f"{team}: {rating}")
