from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('veggie_recipe_book.web.urls')),
    path("profile/", include('veggie_recipe_book.profiles.urls')),
    path("recipe", include('veggie_recipe_book.recipes.urls')),

]
