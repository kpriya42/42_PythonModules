#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    test_inputs = ["25", "abc", "100", "-50"]

    for temp in test_inputs:
        print(f"\nInput data is '{temp}'")

        try:
            temperature = input_temperature(temp)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
