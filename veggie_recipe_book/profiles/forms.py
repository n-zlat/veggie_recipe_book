from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import PasswordInput

from .models import Profile

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            profile = Profile.objects.create(user=user)
            profile.user = user
            profile.save()
        return user


class ProfilePictureForm(forms.ModelForm):
    username = forms.CharField(max_length=35, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['profile_pic', 'username', 'password', 'first_name', 'last_name', 'email']

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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username', 'first_name', 'last_name', )
        widgets = {
            'password': PasswordInput(),
        }
