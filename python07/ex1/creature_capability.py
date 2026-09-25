from abc import ABC, abstractmethod
from ex0.creature_factory import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "") -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.evolved: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str = "itself") -> str:
        return (f"{self.name} heals {target} for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str = "itself & others") -> str:
        return (f"{self.name} heals {target} for a large amount")


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        sp_obj = Sproutling("Sproutling", "Grass")
        return sp_obj

    def create_evolved(self) -> Creature:
        bl_obj = Bloomelle("Bloomelle", "Grass/Fairy")
        return bl_obj


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.evolved is True:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        self.evolved = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.evolved = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.evolved is True:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self.evolved = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.evolved = False
        return "Morphagon stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        sh_obj = Shiftling("Shiftling", "Normal")
        return sh_obj

    def create_evolved(self) -> Creature:
        mp_obj = Morphagon("Morphagon", "Normal/Dragon")
        return mp_obj
