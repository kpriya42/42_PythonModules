#!/usr/bin/env python3

_GRN = "\033[92m"  # bright green
_RED = "\033[91m"  # bright red
_RST = "\033[0m"   # reset
grow_map = {"Rose": 8, "Oak": 1, "Sunflower": 30}
age_map = {"Sunflower": 20}


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def grow(self) -> None:
            self._grow = self._grow + 1

        def age(self) -> None:
            self._age = self._age + 1

        def show(self) -> None:
            self._show = self._show + 1

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self.set_height(height)
        self._age = 0
        self.set_age(age)
        self.stats = Plant.Stats()

    def show(self) -> None:
        self.stats.show()
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        if self.name in grow_map:
            self._height = self._height + grow_map[self.name]
        else:
            self._height = self._height + 1
        self.stats.grow()

    def age(self) -> None:
        if self.name in age_map:
            self._age = self._age + age_map[self.name]
        else:
            self._age = self._age + 1
        self.stats.age()

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            if self._height != 0.0:
                print(f"Height updated: {height}")
            self._height = height

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            if self._age != 0:
                print(f"Age updated: {age}")
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return (self._age)

    @staticmethod
    def check_age(age: int) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def create_unkwn_plant(cls) -> "Plant":
        print("\n=== Anonymous Plant ===")
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, age: int, height: float, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color.capitalize()
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.blooming is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet...")


class Seed(Flower):
    def __init__(self, name: str, age: int, height: float, color: str,
                 seeds: int) -> None:
        super().__init__(name, age, height, color)
        self._seeds = seeds

    def bloom(self) -> None:
        was_blooming = self.blooming
        if not was_blooming:
            self._seeds = 42
        super().bloom()

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class Statistics(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def shade(self) -> None:
            self._shade = self._shade + 1

        def display(self) -> None:
            super().display()
            print(f"  {self._shade} shade")

    def __init__(self, name: str, age: int, height: float,
                 diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter
        self.shade = False
        self.stats: Tree.Statistics = Tree.Statistics()

    def produce_shade(self) -> None:
        self.stats.shade()
        self.shade = True
        print(f"Tree Oak now produces a shade of {self._height:.1f}cm long"
              f" and {self.diameter:.1f}cm wide.")

    def show(self) -> None:
        print("\n=== Tree ===")
        super().show()
        print(f" Trunk diameter: {self.diameter:.1f}")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self, option: bool = False) -> None:
        super().show()
        if option is True:
            print(" Harvest season: " + self.harvest_season)
            print(" Nutritional value:", self.nutritional_value)


if __name__ == '__main__':
    print("=== Garden statistics ===")
    print("=== Check year-old === ")
    print(f"Is 30 days more than a year? {_RED}{Plant.check_age(30)}{_RST}")
    print(f"Is 400 days more than a year? {_GRN}{Plant.check_age(400)}{_RST}")

    print("\n=== Flower ===")
    rose = Flower("Rose", 10, 15.0, "red")
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()

    oak = Tree("Oak", 365, 200.0, 5.0)
    oak.show()
    print("[statistics for Oak]")
    oak.stats.display()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.stats.display()

    print("\n=== Seed ===")
    Sunflower = Seed("Sunflower", 45, 80.0, "yellow", 0)
    Sunflower.show()
    print("[make Sunflower grow, age and bloom]")
    Sunflower.grow()
    Sunflower.age()
    Sunflower.bloom()
    Sunflower.show()
    print("[statistics for Sunflower]")
    Sunflower.stats.display()

    anonymous_plant = Plant.create_unkwn_plant()
    anonymous_plant.show()
    print("[statistics for Unknown plant]")
    anonymous_plant.stats.display()
