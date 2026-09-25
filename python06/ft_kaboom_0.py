#!/usr/bin/env python3

import alchemy.grimoire


def ft_kabm_0() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire directly")

    spell = "Fantasy"
    ingr = "Earth, wind and fire"
    print("Testing record light spell: ", end='')
    print(f"{alchemy.grimoire.light_spell_record(spell, ingr)}")


if __name__ == "__main__":
    ft_kabm_0()
