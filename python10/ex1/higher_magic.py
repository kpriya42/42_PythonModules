#!usr/bin/env python3
from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fire cast on {target} with power {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def meteor(target: str, power: int) -> str:
    return f"Meteor destroys {target} with power {power}"


def condition(target: str, power: int) -> bool:
    return (power >= 20 and len(target) > 0)


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]) \
                   -> Callable[[str, int], tuple[str, str]]:
    """
    Combines two spell functions into one.
    """
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spell


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    """
    Amplifies the power of a spell function by a given multiplier.
    """
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)

    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]) \
                        -> Callable[[str, int], str]:
    """
    Creates a conditional spell caster that
    only casts the spell if the condition is met.
    """
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable[[str, int], str]]) \
        -> Callable[[str, int], list[str]]:
    """
    Creates a sequence of spells to be cast in order.
    """
    def sequence_caster(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence_caster


def main() -> None:

    print("--- Testing spell_combiner ---")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))

    print("\n--- Testing power_amplifier ---")
    mega_fireball = power_amplifier(fireball, 3)
    print(mega_fireball("Goblin", 100))

    print("\n--- Testing conditional_caster ---")
    cast = conditional_caster(condition, fireball)
    print(cast("Wizard", 25))
    print(cast("Knight", 9))

    print("\n--- Testing spell_sequence ---")
    seq = spell_sequence([heal, fireball, meteor])
    print(seq("wizard", 40))


if __name__ == "__main__":
    main()
