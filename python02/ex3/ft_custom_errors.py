#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")

    for function in [check_plant, check_water]:
        try:
            function()
        except GardenError as error:
            print(f"Caught GardenError: {error}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
