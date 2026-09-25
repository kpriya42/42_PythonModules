from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    output: str = "Healing potion brewed with '" + \
                   create_earth() + "' and '" + \
                   create_air() + "'"
    return (output)


def strength_potion() -> str:
    return ("Strength potion brewed with "
            f"'{create_fire()}' and '{create_water()}'")
