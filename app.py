"""
Project Gridiron

Main Application
Version 1.0
"""

print("=" * 50)
print("🏈 PROJECT GRIDIRON")
print("=" * 50)

print("\nLoading NFL teams...")

from data.nfl_ratings import nfl_ratings

print(f"{len(nfl_ratings)} NFL teams loaded.")

print("\nTop 5 Teams (Current Elo)\n")

top_teams = sorted(
    nfl_ratings.items(),
    key=lambda x: x[1],
    reverse=True
)

for team, rating in top_teams[:5]:
    print(f"{team}: {rating}")

print("\nProject Gridiron initialized successfully.")
