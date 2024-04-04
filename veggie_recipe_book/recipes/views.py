from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from .forms import RecipeForm
from .models import Recipe


# class AddIngredientView(LoginRequiredMixin, CreateView):
#     model = Recipe
#     form_class = RecipeForm
#     template_name = 'recipes/add_ingredient.html'
#
#     def form_valid(self, form):
#         recipe_pk = self.kwargs.get('recipe_pk')
#         recipe = Recipe.objects.get(pk=recipe_pk)
#         form.instance.recipe = recipe
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('details_recipe', kwargs={'pk': self.kwargs['recipe_pk']})


# class EditIngredientView(LoginRequiredMixin, UpdateView):
#     model = Recipe
#     form_class = RecipeForm
#     template_name = 'recipes/edit_ingredient.html'
#
#     def get_success_url(self):
#         return reverse_lazy('details_recipe', kwargs={'pk': self.kwargs['recipe_pk']})


class AddRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('details_recipe', kwargs={'pk': self.object.pk}))


class EditRecipeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/edit_recipe.html'
    # success_url = reverse_lazy('details_recipe')

    def get_success_url(self):
        return reverse('details_recipe', kwargs={'pk': self.object.pk})

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class DeleteRecipeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'

    def get_success_url(self):
        return reverse('details_profile', kwargs={'pk': self.object.author.pk})

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class DetailRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/detail_recipe.html'

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        recipe = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return recipe
