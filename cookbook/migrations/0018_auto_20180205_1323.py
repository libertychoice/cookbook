# Generated by Django 2.0.1 on 2018-02-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0017_remove_recipesearchmodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
