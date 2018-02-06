# Generated by Django 2.0.1 on 2018-02-06 14:00

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('cookbook', '0019_auto_20180205_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipesearchmodel',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipesearchmodel',
            name='ingredient',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.',
                                                  through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]