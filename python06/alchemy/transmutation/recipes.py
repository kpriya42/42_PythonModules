import elements
from alchemy import potions
from ..elements import create_air


def lead_to_gold() -> str:
    output = "Recipe transmuting Lead to Gold: brew '" + \
        create_air() + "' and '" + potions.strength_potion() + \
        "' mixed with '" + elements.create_fire() + "'"
    return output
