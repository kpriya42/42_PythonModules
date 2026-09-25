#!usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    sorted(iterable, key=a func(opt), reverse=true or false(opt))
    lambda arguments : expression
    """
    return sorted(artifacts, key=lambda x: x['power'])


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    """
    filter(function, iterable)
    returns an iterator where the items are filtered through a function
    to test if the item is accepted or not.
    """
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    map(function, iterables)
    executes a specified function for each item in an iterable
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_power = max(map(lambda x: x['power'], mages)) if mages else 0
    min_power = min(map(lambda x: x['power'], mages)) if mages else 0
    avg_power = sum(map(lambda x: x['power'], mages)) / len(mages) \
        if mages else 0

    return {'max_power': max_power,
            'min_power': min_power,
            'avg_power': round(avg_power, 2)}


def main() -> None:

    artifacts = [{'name': 'Ice Wand', 'power': 71, 'type': 'relic'},
                 {'name': 'Crystal Orb', 'power': 68, 'type': 'accessory'},
                 {'name': 'Wind Cloak', 'power': 79, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 97, 'type': 'relic'}]
    mages = [{'name': 'Riley', 'power': 69, 'element': 'ice'},
             {'name': 'River', 'power': 93, 'element': 'earth'},
             {'name': 'Ash', 'power': 98, 'element': 'shadow'},
             {'name': 'Casey', 'power': 87, 'element': 'earth'},
             {'name': 'Phoenix', 'power': 64, 'element': 'light'}]
    spells = ['lightning', 'tsunami', 'shield', 'heal']

    print("--- Testing artifact sorter ---")
    sorted_artifacts = artifact_sorter(artifacts)
    for item in sorted_artifacts:
        print(item)

    print("\n--- Testing power filter ---")
    filtered_mages = power_filter(mages, 90)
    for item in filtered_mages:
        print(item)

    print("\n--- Testing spell transformer ---")
    print(spell_transformer(spells))

    print("\n--- Testing mage stats ---")
    print(mage_stats(mages))
    print(mage_stats([]))


if __name__ == "__main__":
    main()
