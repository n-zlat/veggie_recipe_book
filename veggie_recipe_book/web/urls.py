from django.urls import path
from veggie_recipe_book.web.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
