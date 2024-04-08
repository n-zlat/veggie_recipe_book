from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
from veggie_recipe_book.recipes.models import Recipe
from veggie_recipe_book.web.forms import RecipeSearchForm


class HomeView(ListView):
    template_name = 'web/index.html'
    context_object_name = 'recipes'
    paginate_by = 12

    def get_queryset(self):
        queryset = (Recipe.objects.filter(is_private=False)
                    .order_by('-created_at'))

        search_query = self.request.GET.get('search_query')
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        if self.request.GET.get('veggie_recipes'):
            queryset = queryset.filter(author__username='veggie_recipes')
        elif self.request.GET.get('other_users'):
            queryset = queryset.exclude(author__username='veggie_recipes')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeSearchForm(self.request.GET)

        return context


