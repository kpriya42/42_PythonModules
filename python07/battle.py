#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def ft_battle(fact_obj1: CreatureFactory, fact_obj2: CreatureFactory) -> None:
    cr_base1 = fact_obj1.create_base()
    cr_base2 = fact_obj2.create_base()

    print(cr_base1.describe(), " vs.", cr_base2.describe(),
          "Fight!", cr_base1.attack(), cr_base2.attack(), sep='\n')


def ft_instantiate_creatures(fact_obj: CreatureFactory) -> None:
    cr_base = fact_obj.create_base()
    print(f"{cr_base.describe()}")
    print(f"{cr_base.attack()}")

    cr_evol = fact_obj.create_evolved()
    print(f"{cr_evol.describe()}")
    print(f"{cr_evol.attack()}")


if __name__ == "__main__":
    print("Testing factory...")
    fl_factory = FlameFactory()
    ft_instantiate_creatures(fl_factory)

    print("\nTesting factory...")
    aq_factory = AquaFactory()
    ft_instantiate_creatures(aq_factory)

    print("\nTesting battle...")
    ft_battle(fl_factory, aq_factory)
