# Generated by Django 2.0.1 on 2018-02-17 09:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0020_auto_20180206_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientbase',
            name='tag',
        ),
        migrations.DeleteModel(
            name='IngredientBase',
        ),
    ]