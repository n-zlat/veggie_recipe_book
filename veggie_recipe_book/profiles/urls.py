from django.urls import path
from veggie_recipe_book.profiles.views import (
    SignInUserView,
    SignUpUserView,
    DetailsProfileView,
    ProfileUpdateView,
    DeleteProfileView, signout_user,
)

urlpatterns = [
    path('sign-in/', SignInUserView.as_view(), name='sign_in'),
    path('sign-up/', SignUpUserView.as_view(), name='sign_up'),
    path('sign-out/', signout_user, name='sign_out'),
    path('details/<int:pk>/', DetailsProfileView.as_view(), name='details_profile'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('delete/<int:pk>/', DeleteProfileView.as_view(), name='delete_profile'),
]
