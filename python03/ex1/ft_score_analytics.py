#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    print("\n=== Player Score Analytics ===\n")
    scores = []
    if len(sys.argv) != 1:
        arguments = sys.argv[1:]
        index = 0
        while index < len(arguments):
            try:
                score = int(arguments[index])
                scores.append(score)
            except ValueError:
                print(f"Invalid parameter: '{arguments[index]}'")
            index += 1

    if len(scores) != 0:
        total_score = sum(scores)
        average_score = total_score / len(scores)
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}\n")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
