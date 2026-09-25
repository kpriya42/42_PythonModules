#!/usr/bin/env python3

import alchemy.transmutation.recipes


def ft_trans_0() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print("Testing lead to gold: ", end='')
    print(f"{alchemy.transmutation.recipes.lead_to_gold()}")


if __name__ == "__main__":
    ft_trans_0()
