from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model

from veggie_recipe_book.recipes.validators import validate_image_size

UserModel = get_user_model()


class Recipe(models.Model):

    MIN_RECIPE_TITLE_LENGTH = 2
    MAX_RECIPE_TITLE_LENGTH = 75

    class RecipeType(models.TextChoices):
        BAKED_GOODS = 'BG', 'Baked Goods'
        DESSERTS = 'DS', 'Desserts'
        SIDES = 'SD', 'Sides'
        MAINS = 'MN', 'Mains'
        DRINKS = 'DR', 'Drinks'

        @classmethod
        def max_length(cls):
            return max(len(choice[0]) for choice in cls.choices)

    MAX_RECIPE_TYPE_LENGTH = RecipeType.max_length()

    title = models.CharField(max_length=MAX_RECIPE_TITLE_LENGTH,
                             unique=True,
                             blank=False,
                             null=False,
                             validators=[MinLengthValidator(MIN_RECIPE_TITLE_LENGTH,
                                                            message=f'Title cannot be fewer '
                                                                    f'than {MIN_RECIPE_TITLE_LENGTH} letters long'
                                                            ),
                                         ],
                             )
    recipe_type = models.CharField(max_length=MAX_RECIPE_TYPE_LENGTH,
                                   choices=RecipeType.choices,
                                   blank=False,
                                   null=False,
                                   )
    picture = models.ImageField(upload_to='recipe_pictures/',
                                blank=True,
                                null=True,
                                validators=[validate_image_size,
                                            ],
                                )
    ingredients_text = models.TextField(blank=False,
                                        null=False,
                                        )
    description = models.TextField(blank=False,
                                   null=False,
                                   )
    servings = models.IntegerField(blank=False,
                                   null=False,
                                   )
    is_private = models.BooleanField(default=False,
                                     blank=False,
                                     null=False,
                                     )
    created_at = models.DateTimeField(auto_now_add=True,
                                      )
    edited_at = models.DateTimeField(auto_now=True,
                                     )
    author = models.ForeignKey(UserModel,
                               on_delete=models.CASCADE,
                               )

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.ingredients_text:
            ingredients_list = self.ingredients_text.strip()
            self.ingredients = ingredients_list


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               )
    content = models.TextField(blank=False,
                               null=False,
                               )
    created_at = models.DateTimeField(auto_now_add=True,
                                      )
    edited_at = models.DateTimeField(auto_now=True,
                                     )
    user = models.ForeignKey(UserModel,
                             on_delete=models.CASCADE,
                             )

    def clean(self):
        if not self.content.strip():
            raise ValidationError("Comment cannot be empty!")


class Like(models.Model):
    user = models.ForeignKey(UserModel,
                             on_delete=models.CASCADE,
                             )
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'recipe']

    def __str__(self):
        return f'{self.user.username} liked {self.recipe.title}'
