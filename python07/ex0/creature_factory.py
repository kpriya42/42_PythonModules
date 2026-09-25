from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self._type: str = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self._type} type Creature")


class Flameling(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        fl_obj = Flameling("Flameling", "Fire")
        return (fl_obj)

    def create_evolved(self) -> Creature:
        py_ojb = Pyrodon("Pyrodon", "Fire/Flying")
        return (py_ojb)


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        aq_obj = Aquabub("Aquabub", "Water")
        return (aq_obj)

    def create_evolved(self) -> Creature:
        tor_obj = Torragon("Torragon", "Water")
        return (tor_obj)
