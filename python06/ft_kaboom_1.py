#!/usr/bin/env python3

def ft_kabm_1() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    from alchemy.grimoire.dark_spellbook import dark_spell_record

    spell = "Crucio"
    ingr = "wand and potion"
    print("Testing record dark spell: ", end='')
    print(f"{dark_spell_record(spell, ingr)}")


if __name__ == "__main__":
    ft_kabm_1()
