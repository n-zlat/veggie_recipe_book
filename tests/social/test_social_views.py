from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from veggie_recipe_book.recipes.models import Recipe, Like
from veggie_recipe_book.social.forms import CommentForm


class AddCommentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password')
        self.recipe = Recipe.objects.create(title='Test Recipe', author=self.user, servings=4)
        self.url = reverse('add_comment', kwargs={'recipe_id': self.recipe.pk})
        self.client.login(username='test_user', password='password')

    def test_add_comment_view_with_empty_content_stays_on_page(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 200)

    def test_comment_form_valid(self):
        form_data = {'content': 'This is a valid comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

