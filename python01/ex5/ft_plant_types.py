#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self.set_height(height)
        self._age = 0
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = self._height + 0.8

    def age(self) -> None:
        self._age = self._age + 1

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            if self._height != 0:
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


class Tree(Plant):
    def __init__(self, name: str, age: int, height: float,
                 diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter
        self.shade = False

    def produce_shade(self) -> None:
        self.shade = True
        if self.shade is True:
            print(f"Tree Oak now produces a shade of {self._height:.1f}cm long"
                  f" and {self.diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.diameter:.1f}")


class Vegetable(Plant):
    def __init__(self, name: str, age: int, height: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 15

    def show(self, option: bool = False) -> None:
        super().show()
        if option is True:
            print(" Harvest season: " + self.harvest_season)
            print(" Nutritional value:", self.nutritional_value)


if __name__ == '__main__':
    print("=== Garden Plant Types ===\n")
    print("=== Flower")
    rose = Flower("Rose", 10, 15.0, "black")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 365, 200, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    spar = Vegetable("Spargel", 1, 2.0, "April", 0)
    spar.show(True)
    print("[make spargel grow and age for 5 days]")
    for i in range(5):
        spar.grow()
        spar.age()
        spar.show(i == 4)
