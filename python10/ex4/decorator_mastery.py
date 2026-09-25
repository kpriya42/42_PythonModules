#!usr/bin/env python3
from functools import wraps
from collections.abc import Callable
from typing import Any
import time
# import random


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"  Casting {func.__name__}...")

        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"  Spell completed in {elapsed_time:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[[Callable[..., Any]],
                                                Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[0] >= min_power:
                return func(*args, **kwargs)
            return ("  Insufficient power for this spell")

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[[Callable[..., Any]],
                                               Callable[..., Any]]:

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for count in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if count < max_attempts:
                        print("  Spell failed, retrying..."
                              f" (count {count}/{max_attempts})")
            return (f"  Spell casting failed after {max_attempts} attempts")

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def reverse_args(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return reverse_args(power, spell_name)  # type: ignore[no-any-return]


def main() -> None:
    print("\n**** Testing spell timer **** ")

    @spell_timer
    def fireball() -> str:
        time.sleep(1)
        return ("Fireball cast!")
    print("  Result :", fireball())

    # ================================================================================
    print("\n**** Testing power validator **** ")

    @power_validator(100)
    def heavy_strike(power: int, target: str) -> str:
        return f"  Heavy Strike hits {target} with {power} power!"

    print(heavy_strike(120, "Goblin"))
    print(heavy_strike(60, "Dragon"))

    # ================================================================================
    print("\n**** Testing retrying spell **** ")

    @retry_spell(3)
    def wow_spell() -> str:
        return ("  Waaaaaaagh spelled !")

    @retry_spell(3)
    def not_so_wow_spell() -> str:
        raise (RuntimeError("Need to retry.."))

    print(not_so_wow_spell())
    # def battle_cry() -> str:
    #     check = random.randint(0, 2)
    #     if check == 1:
    #         return ("Waaaaaaagh spelled !")
    #     raise (RuntimeError("Need to retry.."))

    print(wow_spell())

    # ================================================================================
    print("\n**** Testing MageGuild **** ")

    mage = MageGuild()

    print(" ", mage.validate_mage_name("Cassia"))
    print(" ", mage.validate_mage_name("Le"))
    print(" ", mage.cast_spell("tornado", 15))
    print(mage.cast_spell("flash", 7))


if __name__ == "__main__":
    main()
