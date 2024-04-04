from django.urls import path
from .views import (AddRecipeView,
                    EditRecipeView,
                    DeleteRecipeView,
                    DetailRecipeView,
                    )

urlpatterns = [
    path('recipe/add/', AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/edit/', EditRecipeView.as_view(), name='edit_recipe'),
    path('recipe/<int:pk>/delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
    path('recipe/<int:pk>/', DetailRecipeView.as_view(), name='details_recipe'),

]
