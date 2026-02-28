import math


def count_len(data: list | tuple | str) -> int:
    i = 0
    for element in data:
        i += 1
    return i


def coordinates_parser(coordinates: str) -> tuple:
    try:
        parsed = coordinates.split(",")
        if count_len(parsed) != 3:
            raise ValueError("invalid coordinates")
        i = 0
        while i < count_len(parsed):
            parsed[i] = int(parsed[i])
            i += 1
        parsed = tuple(parsed)
        print(f"Parsed position: {parsed}")
    except ValueError as e:
        message, = e.args
        print(f"Error parsing coordinates: {message}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
    return tuple(parsed)


def coordinate_system(coordinates: list) -> tuple[int, int, int]:
    if count_len(coordinates) != 3:
        raise ValueError("the cooredinates must has 3 numbers")
    i = 0
    while i < count_len(coordinates):
        coordinates[i] = int(coordinates[i])
        i += 1
    print(f"Position created: {tuple(coordinates)}")
    return tuple(coordinates)


def count_distance(coordinates: list, coordinates_two: list) -> None:
    x1, y1, z1 = coordinates
    x2, y2, z2 = coordinates_two
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {tuple(coordinates_two)} and "
          f"{tuple(coordinates)}: {distance:.2f}")


def position_tracker() -> None:
    try:
        coordinates = [10, 20, 5]
        coordinates_two = [0, 0, 0]
        coordinates_tuple = coordinate_system(coordinates)
        count_distance(coordinates, coordinates_two)
        print()
        coordinate_str = "3,4,0"
        print(f'Parsing coordinates: "{coordinate_str}"')
        coordinates_tuple = coordinates_parser(coordinate_str)
        count_distance(coordinates_tuple, coordinates_two)
        print()
        invalid_coordinates = "abc,def,ghi"
        print(f"Parsing invalid coordinates: {invalid_coordinates}")
        coordinates_parser(invalid_coordinates)
        print()
        print("Unpacking demonstration:")
        x, y, z = coordinates
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as error:
        print(f"Error : {error}")


def main() -> None:
    try:
        position_tracker()
    except Exception as error:
        print(f"Errorfsvreg : {error}")


main()
