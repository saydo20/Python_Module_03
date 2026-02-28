def achievement_tracker(alice: list, bob: list, charlie: list) -> None:
    alice = set(alice)
    bob = set(bob)
    charlie = set(charlie)
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    print()
    common = alice.intersection(bob, charlie)
    print(f"Common to all players: {common}")
    rare = (
        (alice - bob - charlie)
        .union(bob - alice - charlie)
        .union(charlie - alice - bob)
    )
    print(f"Rare achievements (1 player): {rare}")
    print()
    alice_bob_common = alice.intersection(bob)
    print(f"Alice vs Bob common: {alice_bob_common}")
    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


def achievement_tracker_test() -> None:
    alice = ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon']
    bob = ['first_kill', 'level_10', 'boss_slayer', 'collector']
    charlie = ['level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist']
    achievement_tracker(alice, bob, charlie)


def main() -> None:
    try:
        achievement_tracker_test()
    except Exception as error:
        print(f"Error : {error}")


main()
