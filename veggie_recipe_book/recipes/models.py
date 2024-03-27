from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import get_user_model

from veggie_recipe_book.recipes.validators import validate_image_size

UserModel = get_user_model()


class Ingredient(models.Model):
    MIN_INGREDIENT_NAME_LENGTH = 2
    MAX_INGREDIENT_NAME_LENGTH = 50
    MAX_ADDITIONAL_CONTEXT_LENGTH = 100

    class MeasurementUnit(models.TextChoices):
        CUPS = 'cups', 'Cups'
        TBS = 'tbs', 'Tablespoons'
        TS = 'ts', 'Teaspoons'
        PINCH = 'pinch', 'Pinch'
        ML = 'ml', 'Milliliters'
        L = 'l', 'Liters'
        G = 'g', 'Grams'
        KG = 'kg', 'Kilograms'

        @classmethod
        def max_length(cls):
            return max(len(choice[0]) for choice in cls.choices)

    MAX_MEASUREMENT_UNITS_LENGTH = MeasurementUnit.max_length()

    name = models.CharField(max_length=MAX_INGREDIENT_NAME_LENGTH,
                            unique=True,
                            blank=False,
                            null=False,
                            validators=[MinLengthValidator(MIN_INGREDIENT_NAME_LENGTH,
                                                           message=f'Ingredient name cannot be fewer '
                                                                   f'than {MIN_INGREDIENT_NAME_LENGTH} letters long'
                                                           ),
                                        ],
                            help_text="Ingredient Name",
                            )
    measurement_unit = models.CharField(max_length=MAX_MEASUREMENT_UNITS_LENGTH,
                                        choices=MeasurementUnit,
                                        blank=False,
                                        null=False,
                                        help_text='Measurement Unit',
                                        )
    additional_context = models.CharField(max_length=MAX_ADDITIONAL_CONTEXT_LENGTH,
                                          blank=True,
                                          null=True,
                                          help_text="Chopped, At room temperature, Melted, Etc",
                                          )

    def __str__(self):
        return f'{self.name} - {self.measurement_unit}, {self.additional_context}'


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
                             help_text="Recipe Name",
                             )
    recipe_type = models.CharField(max_length=MAX_RECIPE_TYPE_LENGTH,
                                   choices=RecipeType.choices,
                                   blank=False,
                                   null=False,
                                   help_text="Recipe Type",
                                   )
    picture = models.ImageField(upload_to='recipe_pictures/',
                                blank=True,
                                null=True,
                                validators=[validate_image_size,
                                            ],
                                help_text="Upload a picture",
                                )
    description = models.TextField(blank=False,
                                   null=False,
                                   help_text="Your Recipe",
                                   )
    is_private = models.BooleanField(default=False,
                                     blank=False,
                                     null=False,
                                     )
    created_at = models.DateTimeField(auto_now_add=True,
                                      )
    edited_at = models.DateTimeField(auto_now=True,
                                     )
    ingredients = models.ManyToManyField(Ingredient,
                                         )
    author = models.ForeignKey(UserModel,
                               on_delete=models.CASCADE,
                               )

    def __str__(self):
        return self.title


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               )
    content = models.TextField(blank=False,
                               null=False,
                               help_text="Your comment",
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
