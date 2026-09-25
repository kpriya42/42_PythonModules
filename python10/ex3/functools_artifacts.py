#!usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from operator import add, mul
from typing import Any
# import time


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) != 0:
        if operation == "add":
            return (reduce(add, spells))
        elif operation == "mul":
            return (reduce(mul, spells))
        elif operation == "max":
            return (reduce(max, spells))
        elif operation == "min":
            return (reduce(min, spells))
        else:
            raise ValueError(f"Unknown operation - {operation} ")
    return 0


def my_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} used on {target} with power {power} "


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) \
        -> dict[str, Callable[..., str]]:

    dark_ench = partial(base_enchantment, 60, "Dark")
    flow_ench = partial(base_enchantment, 80, "Flowing")
    frez_ench = partial(base_enchantment, 30, "Frozen")
    earth_ench = partial(base_enchantment, 20, "Earthen")

    return {'Dark': dark_ench,
            'Flowing': flow_ench,
            'Frozen': frez_ench,
            'Earthen': earth_ench
            }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatch.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatch.register
    def _(arg: list) -> str:   # type: ignore[type-arg]
        return (f"Multi-cast: {len(arg)} spells")

    return dispatch


def main() -> None:
    spell_powers = [40, 31, 35, 39, 40, 13]
    enchantment_types = ['Dark', 'Flowing', 'Frozen', 'Earthen']
    test_targets = ["Dragon", "Goblin", "Wizard", "Knight"]
    fibonacci_tests = [12, 0, 38]

    # ================================================================================
    print("\n**** Testing spell reducer **** ")
    print("  spell_powers = ", spell_powers)
    try:
        print("  Sum = ", spell_reducer(spell_powers, "add"))
        print("  Product = ", spell_reducer(spell_powers, "mul"))
        print("  Max = ", spell_reducer(spell_powers, "max"))
        print("  Min = ", spell_reducer(spell_powers, "min"))
        print("  Min = ", spell_reducer(spell_powers, "modulo"))
    except ValueError as err:
        print(err)

    # ================================================================================
    print("\n**** Testing partial enchanter **** ")
    enchanted = partial_enchanter(my_enchantment)
    for enchantment_type, target in zip(enchantment_types, test_targets):
        print("  ", enchanted[enchantment_type](target))

    # ================================================================================
    print("\n**** Testing memoized fibonacci **** ")
    for num in fibonacci_tests:
        # start_time = time.perf_counter()
        result = memoized_fibonacci(num)
        # end_time = time.perf_counter()
        print(f"  Fib({num}): {result}  ", end='')
        # print(f" dt = {end_time - start_time:.7f} seconds")
        print(memoized_fibonacci.cache_info())

    # ================================================================================
    print("\n*** Testing spell dispatcher ****")
    spell = spell_dispatcher()
    test_args: list[Any] = [42,
                            'fireball',
                            ['heal', 'freeze', 'shield'],
                            {"a": 10}]
    for item in test_args:
        print("  ", spell(item))


if __name__ == "__main__":
    main()
