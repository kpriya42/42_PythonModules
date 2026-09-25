#!/usr/bin/env python3

import sys
import os
import site


def main() -> None:
    if (sys.prefix == sys.base_prefix):
        print("MATRIX STATUS:You're still plugged in")
        print("\nCurrent Python: ", sys.executable)
        print("Virtual Environment: ", os.getenv("VIRTUAL_ENV"), "detected")

        print("\nWARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n")
        print("To enter the construct, run:\n"
              "  python3 -m venv matrix_env\n"
              "  source matrix_env/bin/activate # On Unix\n"
              "  matrix_env\\Scripts\\activate # On Windows\n"
              "\nThen run this program again.")
    else:
        print("\n==========================================")
        print("MATRIX STATUS: Welcome to the construct")
        print("==========================================")

        print("\nCurrent Python: ", sys.executable)
        print("Virtual Environment: ", os.path.basename(sys.prefix))
        # print("Environment Path: ", sys.prefix)
        print("Environment Path: ", os.getenv("VIRTUAL_ENV"))

        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting "
              "the global system.")

        print("\nPackage installation path:\n", site.getsitepackages()[0])


if __name__ == "__main__":
    main()
