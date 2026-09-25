from abc import ABC, abstractmethod
from ex1 import (HealCapability, TransformCapability)
from ex0.creature_factory import Creature


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, cr: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, cr: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, cr: Creature) -> bool:
        if isinstance(cr, Creature):
            return True
        return False

    def act(self,  cr: Creature) -> str:
        if not self.is_valid(cr):
            raise Exception(f"Invalid creature {type(cr).__name__} for "
                            "normal stratergy")
        return cr.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, cr: Creature) -> bool:
        if isinstance(cr, TransformCapability):
            return True
        return False

    def act(self,  cr: Creature) -> str:
        if isinstance(cr, TransformCapability):
            trf_str = cr.transform()
            att_str = cr.attack()
            rev_str = cr.revert()
            return (trf_str + '\n' + att_str + '\n' + rev_str)
        raise Exception(f"Invalid creature {type(cr).__name__} for "
                        "aggressive stratergy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, cr: Creature) -> bool:
        if isinstance(cr, HealCapability):
            return True
        return False

    def act(self,  cr: Creature) -> str:
        if isinstance(cr, HealCapability):
            att_str = cr.attack()
            heal_str = cr.heal()
            return (att_str + '\n' + heal_str)
        raise Exception(f"Invalid creature {type(cr).__name__} for "
                        "defensive stratergy")
