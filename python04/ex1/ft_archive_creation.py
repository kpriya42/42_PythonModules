#!/usr/bin/env python3

import sys
import typing


def ft_achive_creation(content: str) -> None:
    new_file_name = input("Enter new file name (or empty): ")
    newfile: typing.IO[str] | None = None
    if new_file_name:
        try:
            newfile = open(new_file_name, "w")
            print(f"Saving data to '{new_file_name}'")
            newfile.write(content)
            print(f"Data saved in file '{new_file_name}'")
        except Exception as error:
            print(f"Error opening file '{new_file_name}': {error}")
            return
        finally:
            if newfile is not None:
                newfile.close()
    else:
        print("Not saving data.")


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
            if content[-1] != "\n":
                content = content + '#'
            content = content.replace("\n", "#\n")
            print(f"Transform data:\n ---\n\n{content}\n---")
            ft_achive_creation(content)


def main() -> None:
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return
    ft_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
