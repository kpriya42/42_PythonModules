#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.old = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f} cm {self.old} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.old = self.old + 1


if __name__ == "__main__":
    original_height = 25
    original_age = 30
    rose = Plant("Rose", original_height, original_age)
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()
    print(f"Growth this week: {round(rose.height - original_height)} cm")
