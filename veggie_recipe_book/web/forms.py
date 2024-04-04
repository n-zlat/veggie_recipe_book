from django import forms


class RecipeSearchForm(forms.Form):
    MAX_LENGTH_SEARCH_QUERY = 75

    search_query = forms.CharField(label='Search',
                                   max_length=MAX_LENGTH_SEARCH_QUERY,
                                   required=False,
                                   )
