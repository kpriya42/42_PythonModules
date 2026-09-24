#!/usr/bin/env python3

import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Generate random game events endlessly."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "move", "grab",
               "use", "swim", "climb", "release"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield name, action


def consume_event(events: list[tuple[str, str]]) \
                -> Generator[tuple[str, str], None, None]:
    """Randomly remove and yield events until the list is empty."""
    while events:
        index = random.randrange(len(events))
        yield events.pop(index)


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for index in range(1000):
        name, action = next(event_generator)
        print(f"Event {index}: Player {name} did action {action}")

    event_list = [next(event_generator) for _ in range(10)]

    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
