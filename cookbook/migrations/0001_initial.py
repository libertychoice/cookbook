# Generated by Django 2.0.1 on 2018-01-22 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryCooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDiet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryGeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryUsing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('count', models.IntegerField(blank=True, default=1)),
                ('measure', models.CharField(blank=True, choices=[('кг', 'кг'), ('грамм', 'грамм')], max_length=200)),
                ('ingr_descr', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(blank=True, max_length=200, verbose_name='Название рецепта')),
                ('shortdescription', models.CharField(blank=True, max_length=200, verbose_name='Краткое описание')),
                ('youtube', models.CharField(blank=True, help_text='Вставьте ссылку на видео с YouTube, если она имеется', max_length=200)),
                ('time', models.CharField(blank=True, max_length=200)),
                ('measure', models.CharField(blank=True, choices=[('минут', 'минут'), ('часов', 'часов'), ('дней', 'дней')], max_length=200)),
                ('alldescr', models.TextField(blank=True, max_length=200)),
                ('count', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('category_cooking', models.ManyToManyField(blank=True, to='cookbook.CategoryCooking')),
                ('category_diet', models.ManyToManyField(blank=True, to='cookbook.CategoryDiet')),
                ('category_geo', models.ManyToManyField(blank=True, to='cookbook.CategoryGeo')),
                ('category_main', models.ManyToManyField(blank=True, to='cookbook.CategoryMain')),
                ('category_using', models.ManyToManyField(blank=True, to='cookbook.CategoryUsing')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe'),
        ),
        migrations.AddField(
            model_name='alldescription',
            name='recipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cookbook.Recipe'),
        ),
    ]