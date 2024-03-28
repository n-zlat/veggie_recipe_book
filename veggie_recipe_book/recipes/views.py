from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from veggie_recipe_book.recipes.models import Recipe, Ingredient


class AddIngredientView(CreateView):
    model = Ingredient
    fields = ['name', 'amount', 'measurement_unit', 'additional_context']
    template_name = 'recipes/add_ingredient_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.kwargs['pk']})


class EditIngredientView(UpdateView):
    model = Ingredient
    fields = ['name', 'amount', 'measurement_unit', 'additional_context']
    template_name = 'recipes/edit_ingredient_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'pk': self.kwargs['recipe_pk']})


class AddRecipeView(CreateView):
    model = Recipe
    fields = ['title', 'recipe_type', 'picture', 'description', 'is_private', 'ingredients']
    template_name = 'recipes/add_recipe_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditRecipeView(UpdateView):
    model = Recipe
    fields = ['title', 'recipe_type', 'picture', 'description', 'is_private', 'ingredients']
    template_name = 'recipes/edit_recipe_form.html'
    success_url = reverse_lazy('home')


class DeleteRecipeView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('home')


class DetailRecipeView(DetailView):
    model = Recipe
    template_name = 'recipes/detail_recipes.html'
