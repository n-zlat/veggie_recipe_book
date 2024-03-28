from django.contrib import admin
from django.contrib.auth import get_user_model
from veggie_recipe_book.profiles.forms import CustomUserCreationForm, CustomUserChangeForm


UserModel = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    model = UserModel
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ('pk', 'email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username', )
    ordering = ('username',)

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password1', 'password2')}),
        ('Personal information', {'fields': ('username', 'first_name', 'last_name', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
