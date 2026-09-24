#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as"
                           " floats in format 'x,y,z': ")
        coordinates: list[str] = user_input.split(",")

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(coordinates[0])
        except ValueError as error:
            print(f"Error on parameter '{coordinates[0].strip()}': {error}")
            continue
        try:
            y = float(coordinates[1])
        except ValueError as error:
            print(f"Error on parameter '{coordinates[1].strip()}': {error}")
            continue
        try:
            z = float(coordinates[2])
        except ValueError as error:
            print(f"Error on parameter '{coordinates[2].strip()}': {error}")
            continue

        return (x, y, z)


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first_pos = get_player_pos()

    print(f"Got the first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, "
          f"Y={first_pos[1]}, "
          f"Z={first_pos[2]}")

    distance_to_center = math.sqrt(
                            first_pos[0] ** 2
                            + first_pos[1] ** 2
                            + first_pos[2] ** 2)
    print(f"Distance to center: {round(distance_to_center, 4)}\n")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    print(f"Got the second tuple: {second_pos}")
    distance_between_positions = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2)
    print("\nDistance between the 2 sets of coordinates: "
          f"{round(distance_between_positions, 4)}")


if __name__ == "__main__":
    ft_coordinate_system()
