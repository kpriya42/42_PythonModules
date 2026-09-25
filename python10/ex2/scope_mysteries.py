#!usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def call_counter() -> int:
        nonlocal count
        count += 1
        return count
    return call_counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulator(delta: int) -> int:
        nonlocal total_power
        total_power = total_power + delta
        return total_power
    return (accumulator)


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchantment(item_name: str) -> str:
        return (enchantment_type + ' ' + item_name)
    return enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    stored_item: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        stored_item[key] = value

    def recall(key: str) -> str:
        if key in stored_item:
            return stored_item[key]
        return "Memory not found"

    return {'store': store,
            'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    # ================================================================================
    print("\nTesting spell accumulator...")
    init = 100
    sp_accum = spell_accumulator(init)
    print(f"Base {init}, add 20: {sp_accum(20)}")
    print(f"Base {init}, add 30: {sp_accum(30)}")

    # ================================================================================
    print("\nTesting enchantment factory...")
    sword = enchantment_factory("Flaming")
    shield = enchantment_factory("Frozen")
    print(sword("Sword"))
    print(shield("Shield"))

    # ================================================================================
    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store secret = 42")
    vault['store']("secret", "42")
    print("Recall 'secret':", vault['recall']("secret"))
    print("Recall 'secret':", vault['recall']("ruby"))


if __name__ == "__main__":
    main()
