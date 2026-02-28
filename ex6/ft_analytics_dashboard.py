players = [
    {
        "name": "alice",
        "score": 2300,
        "status": "active",
        "region": "north",
        "achievements": ["first_kill", "level_10", "boss_slayer", "speed_run",
                         "no_damage"]
    },
    {
        "name": "bob",
        "score": 1800,
        "status": "active",
        "region": "east",
        "achievements": ["first_kill", "level_10", "boss_slayer"]
    },
    {
        "name": "charlie",
        "score": 2150,
        "status": "active",
        "region": "central",
        "achievements": ["first_kill", "level_10", "boss_slayer", "speed_run",
                         "no_damage", "legend", "combo_master"]
    },
    {
        "name": "diana",
        "score": 2050,
        "status": "inactive",
        "region": "north",
        "achievements": ["first_kill", "level_10", "boss_slayer", "speed_run"]
    },
]


def list_comprehension(players: list) -> None:
    print("=== List Comprehension Examples ===")

    high_score_value = 2000
    high_score = [hs["name"] for hs in players
                  if hs["score"] >= high_score_value]
    print(f"High scorers ({high_score_value}): {high_score}")

    scores_doubled = [sd["score"] * 2 for sd in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [ap["name"] for ap in players if ap["status"] == "active"]
    print(f"Active players: {active_players}")


def dict_comprehension(players: list) -> None:
    print("=== Dict Comprehension Examples ===")
    player_scores = {player["name"]: player["score"] for player in players}
    print(f"Player scores: {player_scores}")

    ranges = {"high": 2200, "medium": 2000, "low": 0}
    score_categories = {k: sum(1 for p in players
                        if p["score"] >= v) for k, v in ranges.items()}

    print(f"Score categories: {score_categories}")

    achievement_counts = {name["name"]: len(name["achievements"])
                          for name in players}
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension(players: list) -> None:
    print("=== Set Comprehension Examples ===")

    unique_players = {player["name"] for player in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {achievment for player in players
                           for achievment in player["achievements"]}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {region['region'] for region in players}
    print(f"Active regions: {active_regions}")


def combine(players: list) -> None:
    print("=== Combined Analysis ===")
    total_player = len([players for player in players])
    print(f"Total players: {total_player}")

    unique_achievements = len({achievement for player in players
                               for achievement in player["achievements"]
                               })
    print(f"Total unique achievements: {unique_achievements}")

    average_score = sum([score["score"] for score in players]) / total_player
    print(f"Average score : {average_score}")

    max_value = max([score["score"] for score in players])
    result = [top for top in players if top["score"] == max_value][0]
    print(f"Top performer: {result['name']} ({result['score']} pointes,"
          f" {len(result['achievements'])} achievements)")


def analytics_dashboard(players: list) -> None:
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension(players)
    print()
    dict_comprehension(players)
    print()
    set_comprehension(players)
    print()
    combine(players)


def main() -> None:
    try:
        analytics_dashboard(players)
    except Exception as error:
        print(f"error {error}")


main()
