# Generated by Django 5.0.3 on 2024-04-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredient_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1, help_text='Servings'),
            preserve_default=False,
        ),
    ]