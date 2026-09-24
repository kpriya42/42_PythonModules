#!/usr/bin/env python3

import random

players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                      "Gregory", "john", "kevin", "Liam"]


def ft_data_alchemist() -> None:

    capitalized_players: list[str] = [
        player.capitalize()
        for player in players]

    initially_capitalized_players: list[str] = [
        player
        for player in players
        if player.isupper() or player[0].isupper()]

    scores: dict[str, int] = {
        player: random.randint(0, 1000)
        for player in capitalized_players}

    average_score = sum(scores.values()) / len(scores)

    high_scores: dict[str, int] = {
        player: score
        for player, score in scores.items()
        if score > average_score}

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}\n")
    print("New list with all names capitalized: "
          f"{capitalized_players}")

    print("New list of capitalized names only: "
          f"{initially_capitalized_players}\n")

    print(f"Score dict: {scores}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
