#!/usr/bin/env python3

import sys
import typing


def ft_ancient_text(filename: str) -> None:
    file: typing.IO[str] | None = None

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
        content: str = file.read()

        print("---\n")
        print(f"{content}")
        print("---")

    except Exception as error:
        print(f"Error opening file '{filename}': {error}")
        return

    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' is closed.")


def main() -> None:
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    ft_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
