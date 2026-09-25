
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    for ing in allowed_ingredients:
        if ing in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
