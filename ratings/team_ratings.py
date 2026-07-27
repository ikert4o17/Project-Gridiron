def calculate_rating(team):
    rating = (
        team["offense"] * 0.35 +
        team["defense"] * 0.35 +
        team["strength_of_schedule"] * 0.30
    )

    return round(rating, 2)
