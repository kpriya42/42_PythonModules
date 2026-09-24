#!/usr/bin/env python3

import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Treasure Hunter",
    "First Steps",
    "Speed Runner",
    "Survivor",
    "Sharp Mind",
    "Hidden Path Finder"]


def gen_player_achievements() -> set[str]:
    num_of_achievements = random.randint(5, 9)

    # "Untouchable" is assigned to every player so that the intersection
    # is guaranteed to contain at least one achievement.
    player_achiv: set[str] = {"Untouchable"}

    random_achiv = random.sample(
        ACHIEVEMENTS, num_of_achievements)

    player_achiv.update(random_achiv)
    return player_achiv


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")

    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements: set[str] = set().union(alice, bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_achievements}\n")

    common_achiv = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common_achiv}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}\n")

    print(f"Alice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    ft_achievement_tracker()
