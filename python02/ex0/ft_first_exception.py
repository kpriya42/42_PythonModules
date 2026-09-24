#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    valid_input = "25"
    print(f"\nInput data is '{valid_input}'")
    temperature = input_temperature(valid_input)
    print(f"Temperature is now {temperature}°C")

    invalid_input = "abc"
    print(f"\nInput data is '{invalid_input}'")

    try:
        temperature = input_temperature(invalid_input)
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
