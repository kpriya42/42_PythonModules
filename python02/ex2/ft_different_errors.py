#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        print(int("abc"))
    elif operation_number == 1:
        print(100/0)
    elif operation_number == 2:
        print(open('/non/existent/file', 'r'))
    elif operation_number == 3:
        print("Hello " + 123)  # type: ignore[operator]
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for operation_number in range(5):
        print(f"\nTesting operation {operation_number}")
        try:
            garden_operations(operation_number)
            print("Operation completed successfully")

        except ValueError as error:
            print(f"Caught ValueError: {error}")

        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")

        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")

        except TypeError as error:
            print(f"Caught TypeError: {error}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
