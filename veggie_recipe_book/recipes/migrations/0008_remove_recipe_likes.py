# Generated by Django 5.0.3 on 2024-04-09 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_recipe_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
    ]