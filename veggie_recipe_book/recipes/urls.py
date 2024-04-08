from django.urls import path, include
from .views import (AddRecipeView,
                    EditRecipeView,
                    DeleteRecipeView,
                    DetailRecipeView,
                    TypeOfRecipeView,
                    )

urlpatterns = [
    path('add/', AddRecipeView.as_view(), name='add_recipe'),
    path('edit/<int:pk>/edit/', EditRecipeView.as_view(), name='edit_recipe'),
    path('delete/<int:pk>/delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
    path('details/<int:pk>/', DetailRecipeView.as_view(), name='details_recipe'),
    path('recipes-by-type/<str:recipe_type>/', TypeOfRecipeView.as_view(), name='recipes_by_type'),


    path('type/', include([
        path('desserts/', TypeOfRecipeView.as_view(), {'recipe_type': 'DS'}, name='desserts'),
        path('baked-goods/', TypeOfRecipeView.as_view(), {'recipe_type': 'BG'}, name='baked_goods'),
        path('sides/', TypeOfRecipeView.as_view(), {'recipe_type': 'SD'}, name='sides'),
        path('mains/', TypeOfRecipeView.as_view(), {'recipe_type': 'MN'}, name='mains'),
        path('drinks/', TypeOfRecipeView.as_view(), {'recipe_type': 'DR'}, name='drinks'),

    ])),
]
