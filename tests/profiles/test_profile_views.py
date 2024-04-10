from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from veggie_recipe_book.profiles.models import Profile
from veggie_recipe_book.profiles.forms import CustomUserCreationForm, ProfilePictureForm

UserModel = get_user_model()


class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(username='testuser',
                                                  email='test@example.com',
                                                  password='password')
        self.profile = Profile.objects.create(user=self.user)

    def test_form_saves_new_user_correctly(self):
        form_data = {
            'username': 'new_user',
            'email': 'new_user@example.com',
            'password1': 'new_password',
            'password2': 'new_password',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'new_user')
        self.assertEqual(user.email, 'new_user@example.com')

    def test_profile_picture_form_with_valid_data(self):
        form_data = {'username': 'testuser',
                     'password': 'password',
                     'first_name': 'Hoshi',
                     'last_name': 'Kwon',
                     'email': 'test@example.com'}
        form = ProfilePictureForm(data=form_data, instance=self.profile)
        self.assertTrue(form.is_valid())


class DetailsProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='test_user', email='test@example.com', password='password')
        self.profile = Profile.objects.create(user=self.user, username='test_user', email='test@example.com')

    def test_view_returns_200_for_authenticated_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('details_profile', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, 200)

#