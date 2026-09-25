#!/usr/bin/env python3

import alchemy.transmutation


def ft_trans_1() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Testing lead to gold: ", end='')
    print(f"{alchemy.transmutation.lead_to_gold()}")


if __name__ == "__main__":
    ft_trans_1()
