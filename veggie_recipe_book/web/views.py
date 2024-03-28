from django.views.generic import ListView
from veggie_recipe_book.recipes.models import Recipe


class HomeView(ListView):
    model = Recipe
    template_name = 'web/index.html'
    context_object_name = 'recipes'
    paginate_by = 12

    def get_queryset(self):
        queryset = Recipe.objects.filter(is_private=False)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].values('title', 'picture', 'recipe_type', 'author')
        return context
