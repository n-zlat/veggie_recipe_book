from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import PasswordInput
from veggie_recipe_book.profiles.models import Profile
from django import forms

from veggie_recipe_book.recipes.validators import validate_image_size

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'password1': PasswordInput(),
            'password2': PasswordInput(),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'first_name', 'last_name', )
        widgets = {
            'password': PasswordInput(),
        }


# class ProfilePictureForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_pic']
#
#     def save(self, commit=True):
#         profile = super().save(commit=False)
#         profile.profile_pic = self.cleaned_data['profile_pic']
#         if commit:
#             profile.save()
#         return profile
class ProfilePictureForm(forms.ModelForm):
    username = forms.CharField(max_length=35, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    profile_pic = forms.ImageField(required=False)  # Add this line

    class Meta:
        model = Profile
        fields = ['profile_pic', 'username', 'password', 'first_name', 'last_name', 'email', ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            user = instance.user
            kwargs.setdefault('initial', {}).update({
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            })
        super().__init__(*args, **kwargs)

    def clean_profile_pic(self):
        profile_pic = self.cleaned_data.get('profile_pic')

        return profile_pic

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user

        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        user.save()

        if commit:
            profile.save()
        return profile
