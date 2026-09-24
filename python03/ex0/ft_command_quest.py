#!/usr/bin/env python3

import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        arguments = sys.argv[1:]
        index = 0
        while index < len(arguments):
            print(f"Argument {index + 1}: {arguments[index]}")
            index += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
