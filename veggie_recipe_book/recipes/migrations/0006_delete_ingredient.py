# Generated by Django 5.0.3 on 2024-04-02 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_recipe_ingredients_ingredient_recipe_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
