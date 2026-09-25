#!/usr/bin/env python3

import alchemy


def ft_trans_2() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module directly")
    print("Testing lead to gold: ", end='')
    print(f"{alchemy.lead_to_gold()}")


if __name__ == "__main__":
    ft_trans_2()
