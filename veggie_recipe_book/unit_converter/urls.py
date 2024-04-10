from django.urls import path
from veggie_recipe_book.unit_converter.views import UnitConverterView

urlpatterns = [
    path('', UnitConverterView.as_view(), name='unit_converter'),

]
