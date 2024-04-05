from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('veggie_recipe_book.web.urls')),
    path("profile/", include('veggie_recipe_book.profiles.urls')),
    path("recipe/", include('veggie_recipe_book.recipes.urls')),
    path("social/", include('veggie_recipe_book.social.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)