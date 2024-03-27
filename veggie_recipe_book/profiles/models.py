from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from veggie_recipe_book.profiles.validators import UsernameValidator

UserModel = get_user_model()


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 35
    MIN_USERNAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 30
    MIN_FIRST_NAME_LENGTH = 2
    MAX_LAST_NAME_LENGTH = 50
    MIN_LAST_NAME_LENGTH = 1

    username = models.CharField(max_length=MAX_USERNAME_LENGTH,
                                unique=True,
                                blank=False,
                                null=False,
                                help_text="Your Username",
                                validators=[MinLengthValidator(MIN_USERNAME_LENGTH,
                                                               message=f'Username cannot be fewer '
                                                                       f'than {MIN_USERNAME_LENGTH} letters long'),
                                            UsernameValidator(),
                                            ],
                                )
    first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH,
                                  blank=True,
                                  null=True,
                                  validators=[MinLengthValidator(MIN_FIRST_NAME_LENGTH,
                                                                 message=f'First name cannot be fewer '
                                                                         f'than {MIN_FIRST_NAME_LENGTH} letters long'
                                                                 ),
                                              ],
                                  )
    last_name = models.CharField(max_length=MAX_LAST_NAME_LENGTH,
                                 blank=True,
                                 null=True,
                                 validators=[MinLengthValidator(MIN_LAST_NAME_LENGTH,
                                                                message=f'Last name cannot be fewer '
                                                                        f'than {MIN_LAST_NAME_LENGTH} letters long'
                                                                ),
                                             ],
                                 )
    profile_pic = models.URLField(blank=True,
                                  null=True,
                                  )
    email = models.EmailField(null=False,
                              blank=False,
                              )

    age = models.PositiveIntegerField(null=True,
                                      blank=True,
                                      )
    user = models.OneToOneField(UserModel,
                                primary_key=True,
                                on_delete=models.CASCADE,
                                )
