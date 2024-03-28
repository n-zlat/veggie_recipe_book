from django.urls import path
from .views import (AddRecipeView,
                    EditRecipeView,
                    DeleteRecipeView,
                    DetailRecipeView,
                    EditIngredientView,
                    AddIngredientView,
                    )

urlpatterns = [
    path('recipe/add/', AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/edit/', EditRecipeView.as_view(), name='edit_recipe'),
    path('recipe/<int:pk>/delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
    path('recipe/<int:pk>/', DetailRecipeView.as_view(), name='details_recipe'),
    path('recipe/<int:pk>/addingredient/', AddIngredientView.as_view(), name='add_ingredient'),
    path('recipe/<int:recipe_pk>/ingredient/<int:pk>/edit/', EditIngredientView.as_view(), name='edit_ingredient'),

]
