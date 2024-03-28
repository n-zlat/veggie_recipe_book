from django.contrib import admin
from veggie_recipe_book.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'recipe_type', 'picture', 'created_at', 'is_private', )
    search_fields = ('title', 'author', 'recipe_type', )
    list_filter = ('author', 'is_private', 'recipe_type', )
    ordering = ('-created_at', )
