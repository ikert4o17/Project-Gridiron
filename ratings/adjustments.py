"""
Project Gridiron
Game Adjustments

Version 0.1
"""

HOME_FIELD_ADVANTAGE = 2.5


def apply_home_field(rating, is_home):

    if is_home:
        return rating + HOME_FIELD_ADVANTAGE

    return rating
