# Generated by Django 5.0.3 on 2024-04-03 14:09

import django.core.validators
import veggie_recipe_book.profiles.validators
import veggie_recipe_book.recipes.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/', validators=[veggie_recipe_book.recipes.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(2, message='Username cannot be fewer than 2 letters long'), veggie_recipe_book.profiles.validators.UsernameValidator()]),
        ),
    ]
