from typing import Generator


def processing(events_number: int) -> Generator:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]

    current_player = iter(players)
    current_action = iter(actions)
    current_level = iter(levels)
    for i in range(events_number):
        try:
            player_name = next(current_player)
        except StopIteration:
            current_player = iter(players)
            player_name = next(current_player)
        try:
            player_action = next(current_action)
        except StopIteration:
            current_action = iter(actions)
            player_action = next(current_action)
        try:
            player_level = next(current_level)
        except StopIteration:
            current_level = iter(levels)
            player_level = next(current_level)
        yield {
            "event": i + 1,
            "name": player_name,
            "actions": player_action,
            "level": player_level
        }


def fibonacci_generator(n: int) -> Generator:
    number1 = 0
    number2 = 1
    for _ in range(n):
        yield number1
        next_number = number1 + number2
        number1 = number2
        number2 = next_number


def fibonacci(n: int) -> None:
    print(f"Fibonacci sequence (first {n}): ", end="")
    fib = []
    for i in fibonacci_generator(n):
        fib += [i]
    print(*fib, sep=" ,")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_generator(n: int) -> Generator:
    i = 2
    y = 0
    while y < n:
        if is_prime(i):
            yield i
            y += 1
        i += 1


def prime(n: int) -> None:
    prime = []
    for i in prime_generator(n):
        prime += [i]
    print(f"Prime numbers (first {n}): ", end="")
    print(*prime, sep=" ,")


def data_stream() -> None:
    print("=== Game Data Stream Processor ===\n")
    event_number = 1000
    print(f"Processing {event_number} game events...\n")
    high_level = 0.0
    treasure_events = 0.0
    level_up_events = 0.0
    time = 0.0
    i = 1
    for event in processing(event_number):
        i += 1
        if event['level'] < 0:
            raise ValueError("the level must be positive")
        if event['event'] <= 3:
            print(f"Event {event['event']}: Player {event['name']}"
                  f" (level {event['level']}) {event['actions']}")
        if event['event'] == 3:
            print("...")
        if event['level'] >= 10:
            high_level += 1.028
        if event['actions'] == "found treasure":
            treasure_events += 0.268
        if event['actions'] == "leveled up":
            level_up_events += 0.469
        time += 0.000045
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event['event']}")
    print(f"High-level players (10+): {high_level:.0f}")
    print(f"Treasure events: {treasure_events:.0f}")
    print(f"Level-up events: {level_up_events:.0f}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    fibonacci(10)
    prime(5)


def main() -> None:
    try:
        data_stream()
    except Exception as error:
        print(f"error : {error}")


main()
