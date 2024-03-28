from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from veggie_recipe_book.profiles.forms import CustomUserCreationForm, ProfilePictureForm
from veggie_recipe_book.profiles.models import Profile


UserModel = get_user_model()


class SignInUserView(LoginView):
    template_name = 'profiles/sign_in.html'
    success_url = reverse_lazy('home')


class SignUpUserView(CreateView):
    template_name = 'profiles/sign_up.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        Profile.objects.create(user=form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('home')


class DetailsProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile_details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        context['recipes'] = profile.user.recipe_set.filter(is_private=False)
        context['first_name'] = profile.user.first_name
        context['last_name'] = profile.user.last_name
        context['email'] = profile.user.email

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profiles/edit_profile.html'
    form_class = ProfilePictureForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("details_profile", kwargs={"pk": self.object.pk})


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    queryset = Profile.objects.all()\
        .prefetch_related("user") \
        .all()
    template_name = "profiles/delete_profile.html"
