#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, BattleStrategy)


def battle(participants: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament between", len(participants), "opponents ***")
    i = 0
    while i < len(participants):
        j = i + 1
        while j < len(participants):
            ft_1, st_1 = participants[i]
            ft_2, st_2 = participants[j]
            player1 = ft_1.create_base()
            player2 = ft_2.create_base()
            print("\n     🛡️  Battle")
            print(player1.describe())
            print("            vs.")
            print(player2.describe())
            print("\n     👊 Now Fight")
            try:
                print(st_1.act(player1))
                print(st_2.act(player2))
            except Exception as err:
                print("\n‼️ Battle error, aborting tournament:\n", err)
                return
            j += 1
        i += 1


if __name__ == "__main__":
    fl_factory = FlameFactory()
    aq_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    trans_factory = TransformCreatureFactory()
    n_stratergy = NormalStrategy()
    a_stratergy = AggressiveStrategy()
    d_stratergy = DefensiveStrategy()

    print("\n----------------------------------------------------------------")
    print("Tournament 0 (basic)")
    print("[(Flameling + Normal), (Healing + Defensive)]\n")
    tour0 = [(fl_factory, n_stratergy), (heal_factory, d_stratergy)]
    battle(tour0)

    print("\n----------------------------------------------------------------")
    print("Tournament 1 (error)")
    print("[(Flameling + Aggressive), (Healing + Defensive)]\n")
    tour1 = [(fl_factory, a_stratergy), (heal_factory, d_stratergy)]
    battle(tour1)

    print("\n----------------------------------------------------------------")
    print("Tournament 2 (multiple)")
    print("[(Aquabub + Normal), (Healing + Defensive),"
          " (Transform + Aggressive)]\n")
    tour2 = [(aq_factory, n_stratergy), (heal_factory, d_stratergy),
             (trans_factory, a_stratergy)]
    battle(tour2)
