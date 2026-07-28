"""
Project Gridiron
Stat Converter

Version 0.1
"""


def offense_rating(points_per_game, yards_per_play):

    return round(
        (points_per_game * 2) +
        (yards_per_play * 8),
        2
    )


def defense_rating(points_allowed):

    return round(
        100 - (points_allowed * 2),
        2
    )


def overall_rating(offense, defense):

    return round(
        offense * 0.55 +
        defense * 0.45,
        2
    )
