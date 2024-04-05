from django.urls import path, include
from .views import (AddRecipeView,
                    EditRecipeView,
                    DeleteRecipeView,
                    DetailRecipeView,
                    RecipesByTypeView,
                    )

urlpatterns = [
    path('add/', AddRecipeView.as_view(), name='add_recipe'),
    path('edit/<int:pk>/edit/', EditRecipeView.as_view(), name='edit_recipe'),
    path('delete/<int:pk>/delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
    path('details/<int:pk>/', DetailRecipeView.as_view(), name='details_recipe'),

    path('type/', include([
        path('desserts/', RecipesByTypeView.as_view(), {'recipe_type': 'DS'}, name='desserts'),
        path('baked-goods/', RecipesByTypeView.as_view(), {'recipe_type': 'BG'}, name='baked_goods'),
        path('sides/', RecipesByTypeView.as_view(), {'recipe_type': 'SD'}, name='sides'),
        path('mains/', RecipesByTypeView.as_view(), {'recipe_type': 'MN'}, name='mains'),
        path('drinks/', RecipesByTypeView.as_view(), {'recipe_type': 'DR'}, name='drinks'),
    ])),
]
