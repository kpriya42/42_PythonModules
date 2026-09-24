#!/usr/bin/env python3

import sys


def ft_process_input_params() -> dict[str, int]:
    inventory = {}
    index = 1

    while index < len(sys.argv):
        parameter = sys.argv[index]
        parts = parameter.split(":")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(f"Error - invalid parameter '{parameter}'")
            index += 1
            continue
        item_name = parts[0]
        quantity_text = parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            index += 1
            continue
        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            index += 1
            continue
        inventory.update({item_name: quantity})
        index += 1

    return inventory


def ft_inventory_system() -> None:

    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = ft_process_input_params()

    if len(inventory) > 0:
        print(f"Got inventory: {inventory}")

        item_list = list(inventory.keys())
        print(f"Item list: {item_list}")

        total_quantity = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: "
              f"{total_quantity}")

        if total_quantity != 0:
            for item_name in inventory:
                percentage = inventory[item_name] / total_quantity * 100
                print(f"Item {item_name} represents "
                      f"{round(percentage, 1)}%")

        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item_name in inventory:
            if inventory[item_name] > inventory[most_abundant]:
                most_abundant = item_name
            if inventory[item_name] < inventory[least_abundant]:
                least_abundant = item_name

        print(f"Item most abundant: {most_abundant} "
              f"with quantity {inventory[most_abundant]}")

        print(f"Item least abundant: {least_abundant} "
              f"with quantity {inventory[least_abundant]}")

        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")

    else:
        print("\nNo arguments provided.\nUsage: python3 ft_inventory_system.py"
              " <name1:quantity1> <name2:quantity2> ...\n")


if __name__ == "__main__":
    ft_inventory_system()
