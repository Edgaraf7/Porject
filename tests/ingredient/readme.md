codigo 01

from src.models.ingredient import Ingredient, restriction_map, Restriction


def test_ingredient():
    def test_ingredient_instantiation():
        ingredient = Ingredient("Tomato")
        assert ingredient.name == "Tomato"
        assert ingredient.restrictions == set()

    def test_ingredient_with_known_restrictions():
        ingredient = Ingredient("bacon")
        expected_restrictions = {Restriction.ANIMAL_MEAT,
                                 Restriction.ANIMAL_DERIVED}
        assert ingredient.restrictions == expected_restrictions

    def test_ingredient_with_unknown_restrictions():
        ingredient = Ingredient("apple")
        assert ingredient.restrictions == set()

    def test_ingredient_repr():
        ingredient = Ingredient("Tomato")
        assert repr(ingredient) == "Ingredient('Tomato')"

    def test_ingredient_equality():
        ingredient1 = Ingredient("Tomato")
        ingredient2 = Ingredient("Tomato")
        ingredient3 = Ingredient("Potato")
        assert ingredient1 == ingredient2
        assert ingredient1 != ingredient3

    def test_ingredient_hash():
        ingredient1 = Ingredient("Tomato")
        ingredient2 = Ingredient("Tomato")
        ingredient3 = Ingredient("Potato")
        assert hash(ingredient1) == hash(ingredient2)
        assert hash(ingredient1) != hash(ingredient3)

    def test_restriction_map():
        # Check if all ingredients have their corresponding restrictions
        for ingredient, restrictions in restriction_map().items():
            for restriction in restrictions:
                assert isinstance(restriction, Restriction)

    # Executar todas as funções de teste
    for func in [
        test_ingredient_instantiation,
        test_ingredient_with_known_restrictions,
        test_ingredient_with_unknown_restrictions,
        test_ingredient_repr,
        test_ingredient_equality,
        test_ingredient_hash,
        test_restriction_map
    ]:
        func()


# Executar a função de teste principal
test_ingredient()


codigo 02

from src.models.ingredient import Ingredient, restriction_map, Restriction

def test_ingredient():
    def test_ingredient_instantiation():
        ingredient = Ingredient("Tomato")
        assert ingredient.name == "Tomato"
        assert ingredient.restrictions == set()

    def test_ingredient_equality():
        ingredient1 = Ingredient("Tomato")
        ingredient2 = Ingredient("Tomato")
        ingredient3 = Ingredient("Potato")
        assert ingredient1 == ingredient2
        assert ingredient1 != ingredient3

    def test_ingredient_hash():
        ingredient1 = Ingredient("Tomato")
        ingredient2 = Ingredient("Tomato")
        ingredient3 = Ingredient("Potato")
        assert hash(ingredient1) == hash(ingredient2)
        assert hash(ingredient1) != hash(ingredient3)

    def test_ingredient_with_invalid_repr():
        ingredient = Ingredient("Tomato")
        assert repr(ingredient) == f"Ingredient('{ingredient.name}')"

    def test_restriction_map():
        for restrictions in restriction_map().values():
            assert all(isinstance(restriction, Restriction) for restriction in restrictions)

    for func in [
        test_ingredient_instantiation,
        test_ingredient_equality,
        test_ingredient_hash,
        test_ingredient_with_invalid_repr,
        test_restriction_map
    ]:
        func()

test_ingredient()
