#!/usr/bin/env python3

from ex1 import (HealingCreatureFactory, TransformCreatureFactory,
                 HealCapability, TransformCapability)


def ft_healcap_test() -> None:
    print("  base:")
    heal_factory = HealingCreatureFactory()
    cr_base = heal_factory.create_base()
    print(f"{cr_base.describe()}")
    print(f"{cr_base.attack()}")
    if isinstance(cr_base, HealCapability):
        print(f"{cr_base.heal()}")
    print("  evolved:")
    cr_evol = heal_factory.create_evolved()
    print(f"{cr_evol.describe()}")
    print(f"{cr_evol.attack()}")
    if isinstance(cr_evol, HealCapability):
        print(f"{cr_evol.heal()}")


def ft_transformcap_test() -> None:
    print("  base:")
    trans_factory = TransformCreatureFactory()
    cr_base = trans_factory.create_base()
    print(f"{cr_base.describe()}")
    print(f"{cr_base.attack()}")
    if isinstance(cr_base, TransformCapability):
        print(f"{cr_base.transform()}")
        print(f"{cr_base.attack()}")
        print(f"{cr_base.revert()}")
    print("  evolved:")
    cr_evol = trans_factory.create_evolved()
    print(f"{cr_evol.describe()}")
    print(f"{cr_evol.attack()}")
    if isinstance(cr_evol, TransformCapability):
        print(f"{cr_evol.transform()}")
        print(f"{cr_evol.attack()}")
        print(f"{cr_evol.revert()}")


if __name__ == "__main__":
    print("Testing Creature with healing capability...")
    ft_healcap_test()
    print("\nTesting Creature with transform capability...")
    ft_transformcap_test()
