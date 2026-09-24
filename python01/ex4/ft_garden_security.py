#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self.set_height(height)
        self._age = 0
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f} cm {self._age} days old")

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
                print(f"Height updated: {height}cm")
            self._height = height

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            if self._age != 0:
                print(f"Age updated: {age} days")
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return (self._age)


if __name__ == '__main__':
    print("\n=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 5)
    print(f"Plant created: {rose.name}: {rose.get_height()}cm,"
          f" {rose.get_age()} days old\n")
    print("Try to set height to 25cm and age to 30 days")
    rose.set_height(25)
    rose.set_age(30)
    print("\nTry to set height to -10 cm and age to -50 days")
    rose.set_height(-10)
    rose.set_age(-50)
    print()
    print(f"Current state: {rose.name}: {rose.get_height()}cm,"
          f" {rose.get_age()} days old")
