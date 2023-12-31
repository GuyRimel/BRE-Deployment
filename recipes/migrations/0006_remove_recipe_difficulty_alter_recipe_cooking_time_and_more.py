# Generated by Django 4.2.2 on 2023-06-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_genre_recipe_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='difficulty',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(help_text='in minutes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=300),
        ),
    ]
