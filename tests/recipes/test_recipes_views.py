from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from veggie_recipe_book.recipes.models import Recipe

UserModel = get_user_model()


class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(username='test_user', email='test@example.com', password='password')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            recipe_type='DS',
            author=self.user,
            description='Test recipe description',
            servings=4,
            is_private=False,
            ingredients_text='Ingredient 1\nIngredient 2\nIngredient 3',

        )

    def test_add_recipe_view_redirects_home_after_success(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('add_recipe'), {
            'title': 'New Recipe',
            'recipe_type': 'DS',
            'description': 'New recipe description',
            'servings': 2,
            'is_private': False,
            'ingredients_text': 'Ingredient 1\nIngredient 2\nIngredient 3',

        })
        self.assertEqual(response.status_code, 302)

    def test_edit_recipe_view_redirects_home_after_success(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('edit_recipe', kwargs={'pk': self.recipe.pk}), {
            'title': 'Updated Recipe',
            'recipe_type': 'MN',
            'description': 'Updated recipe description',
            'servings': 4,
            'is_private': True,
            'ingredients_text': 'Ingredient 1\nIngredient 2\nIngredient 3',
        })
        self.assertEqual(response.status_code, 302)

    def test_delete_recipe_view_redirects_profile_details_after_success(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('delete_recipe', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 302)

    def test_detail_recipe_view_retrieves_correct_data(self):
        response = self.client.get(reverse('details_recipe', kwargs={'pk': self.recipe.pk}))
        self.assertEqual(response.status_code, 200)

    def test_add_recipe_view_invalid_form_data(self):
        self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('add_recipe'), {})
        self.assertEqual(response.status_code, 200)

    def test_detail_recipe_view_with_recipe_that_does_not_exist(self):
        response = self.client.get(reverse('details_recipe', kwargs={'pk': self.recipe.pk + 65431}))
        self.assertEqual(response.status_code, 404)

