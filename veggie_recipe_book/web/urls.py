from django.urls import path

from veggie_recipe_book.web.views import index

urlpatterns = [
    path('', index),
]
