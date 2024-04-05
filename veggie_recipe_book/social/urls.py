from django.urls import path

from veggie_recipe_book.social.views import AddCommentView, like_recipe, unlike_recipe

urlpatterns = [
    path('recipe/<int:recipe_id>/add-comment/', AddCommentView.as_view(), name='add_comment'),
    path('recipe/<int:recipe_id>/like/', like_recipe, name='recipe_like'),
    path('recipe/<int:recipe_id>/unlike/', unlike_recipe, name='recipe_unlike')
]
