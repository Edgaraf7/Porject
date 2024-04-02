from src.models.ingredient import Ingredient, restriction_map, Restriction


def test_ingredient():
    # Testa a criação de ingredientes e suas propriedades
    ingredient1 = Ingredient("Tomato")
    assert ingredient1.name == "Tomato"
    assert ingredient1.restrictions == set()

    ingredient2 = Ingredient("Tomato")
    assert ingredient1 == ingredient2
    assert hash(ingredient1) == hash(ingredient2)

    ingredient3 = Ingredient("Potato")
    assert ingredient1 != ingredient3
    assert hash(ingredient1) != hash(ingredient3)

    assert repr(ingredient1) == f"Ingredient('{ingredient1.name}')"

    # Testa se o mapeamento de restrições está correto
    for restrictions in restriction_map().values():
        assert all(isinstance
                   (restriction, Restriction) for restriction in restrictions)


test_ingredient()
