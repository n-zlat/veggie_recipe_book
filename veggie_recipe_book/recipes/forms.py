from django import forms

from veggie_recipe_book.recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe_type', 'picture', 'description', 'servings',
                  'is_private', 'ingredients_text']
        widgets = {
            'ingredients_text': forms.Textarea(attrs={'placeholder': 'Please enter each ingredient on a new line.'},
                                               ),
            'title': forms.TextInput(attrs={'placeholder': 'Recipe Name'},
                                     ),
            'description': forms.Textarea(attrs={'placeholder': 'Your recipe'},
                                          ),
        }
