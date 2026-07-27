"""
Project Gridiron
Data Sources

Version 0.1
"""

sources = {
    "nfl": [
        "Schedule",
        "Team Stats",
        "Advanced Metrics",
        "Injuries",
        "Weather",
        "Betting Lines"
    ],

    "college": [
        "Schedule",
        "Team Stats",
        "Advanced Metrics",
        "Conference Strength",
        "Recruiting",
        "Transfer Portal"
    ]
}


def show_sources():

    for league, data in sources.items():
        print(league.upper())

        for item in data:
            print("-", item)


show_sources()
