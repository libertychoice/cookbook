# Generated by Django 2.0.1 on 2018-01-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20180117_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorycooking',
            name='options',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='categorydiet',
            name='options',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='categorygeo',
            name='options',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='categorymain',
            name='options',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
