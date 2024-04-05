from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.views.generic import ListView
from veggie_recipe_book.recipes.models import Recipe
from veggie_recipe_book.web.forms import RecipeSearchForm


class HomeView(ListView):
    model = Recipe
    template_name = 'web/index.html'
    context_object_name = 'recipes'
    paginate_by = 12

    def get_queryset(self):
        queryset = (Recipe.objects.filter(is_private=False).
                    order_by('-created_at'))

        search_query = self.request.GET.get('search_query')
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = RecipeSearchForm(self.request.GET)

        #TODO: paginator common logic
        paginator = Paginator(context['recipes'], self.paginate_by)
        page_number = self.request.GET.get('page')

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context['page_obj'] = page_obj

        return context
