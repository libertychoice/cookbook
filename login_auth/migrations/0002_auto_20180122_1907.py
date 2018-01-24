# Generated by Django 2.0.1 on 2018-01-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=254, unique=True, verbose_name='USERNAME'),
        ),
    ]
