#!/usr/bin/env python3

from alchemy import create_air


def ft_almbc_5() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    ft_almbc_5()
