from django.test import TestCase
from veggie_recipe_book.recipes.forms import RecipeForm


class RecipeFormTestCase(TestCase):
    def test_recipe_form_valid(self):
        form_data = {
            'title': 'Test Recipe',
            'recipe_type': 'DS',
            'description': 'so some baking',
            'servings': 4,
            'is_private': False,
            'ingredients_text': 'eggs\nsugar 2\nspice 3',
        }
        form = RecipeForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_recipe_form_invalid_because_of_no_title(self):
        form_data = {
            'title': '',
            'recipe_type': 'DS',
            'description': 'do some baking',
            'servings': 4,
            'is_private': False,
            'ingredients_text': 'Ingredient 1\nIngredient 2\nIngredient 3',

        }
        form = RecipeForm(data=form_data)
        self.assertFalse(form.is_valid())
