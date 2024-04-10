from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy, reverse
from veggie_recipe_book.recipes.forms import RecipeForm
from veggie_recipe_book.recipes.models import Recipe, Comment, Like
from veggie_recipe_book.social.forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        recipe_type = recipe.recipe_type

        comments = Comment.objects.filter(recipe=recipe)
        context['comments'] = comments
        context['comment_form'] = CommentForm() if self.request.user.is_authenticated else None

        context['has_liked'] = (Like.objects.filter(recipe=recipe, user=self.request.user).exists()) if self.request.user.is_authenticated else False
        total_likes = (Like.objects.filter(recipe=recipe)
                       .count())
        context['total_likes'] = total_likes

        context['recipe_type'] = recipe_type

        return context


class TypeOfRecipeView(ListView):
    template_name = 'recipes/recipes_by_type.html'
    context_object_name = 'recipes'
    paginate_by = 12

    def get_queryset(self):
        recipe_type = self.kwargs.get('recipe_type')
        return ((Recipe.objects
                .filter(recipe_type=recipe_type)
                .filter(is_private=False))
                .order_by('-created_at'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipe_type = self.kwargs.get('recipe_type')
        recipe_type_display = dict(Recipe.RecipeType.choices)[recipe_type]
        context['recipe_type_display'] = recipe_type_display

        return context
