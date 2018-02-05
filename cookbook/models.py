from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager

from login_auth.models import User

# Create your models here.
MAX_LEN_TEXT = 200

CATEGORY_USING_CHOICES = (
    (1, "На обед"),
    (2, "На завтрак")
)

CATEGORY_GEO_CHOICES = (
    (1, "Европейская"),
    (2, "Азиатская")
)

CATEGORY_MAIN_CHOICES = (
    (1, "Вторые блюда"),
    (2, "Салаты")
)

CATEGORY_DIET_CHOICES = (
    (1, "ПП"),
    (2, "Вегетарианские")
)

CATEGORY_COOKING_CHOICES = (
    (1, "Духовка"),
    (2, "Гриль")
)

MEASURE_CHOICES = (
    ("кг", "кг"),
    ("грамм", "грамм")
)

TIME_CHOICES = (
    ("минут", "минут"),
    ("часов", "часов"),
    ("дней", "дней")
)


class CategoryUsing(models.Model):
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryGeo(models.Model):
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryMain(models.Model):
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryDiet(models.Model):
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryCooking(models.Model):
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


def get_path(instance, filename):
    return 'recipes/{}/files/{}'.format(instance.pk, filename)


class RecipeSearchModel(models.Model):
    ingredients = TaggableManager(blank=True, )


class Recipe(models.Model):
    """
    Recipe model
    """
    recipe_name = models.CharField("Название рецепта", blank=True, max_length=200)
    shortdescription = models.CharField("Краткое описание", blank=True, max_length=500)
    youtube = models.CharField(blank=True, help_text="Вставьте ссылку на видео с YouTube, если она имеется",
                               max_length=200)
    category_using = models.ManyToManyField(CategoryUsing, blank=True)
    category_geo = models.ManyToManyField(CategoryGeo, blank=True)
    category_main = models.ManyToManyField(CategoryMain, blank=True)
    category_diet = models.ManyToManyField(CategoryDiet, blank=True)
    category_cooking = models.ManyToManyField(CategoryCooking, blank=True)
    time = models.CharField(blank=True, max_length=200)
    measure = models.CharField(blank=True, max_length=200, choices=TIME_CHOICES)
    alldescr = models.TextField(blank=True, max_length=10000)
    count = models.CharField(blank=True, default="", max_length=200)
    image = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default="")
    datetime = models.DateTimeField("Дата создания", auto_now_add=True, blank=True)  #

    def __str__(self):
        return self.recipe_name

    def get_short_text(self):
        if len(self.shortdescription) > MAX_LEN_TEXT:
            return self.shortdescription[:MAX_LEN_TEXT] + '...'
        else:
            return self.shortdescription


@receiver(pre_save, sender=Recipe)
def replace_youtube_link(sender, instance, **kwargs):
    instance.youtube = instance.youtube.replace("youtu.be", "www.youtube.com/embed")


class IngredientBase(models.Model):
    tag = TaggableManager(blank=True)


class Ingredient(models.Model):
    """
    Ingredient with description
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True)
    name = models.CharField(blank=True, max_length=200)
    count = models.IntegerField(blank=True, default=1)
    measure = models.CharField(blank=True, max_length=200, choices=MEASURE_CHOICES)
    ingr_descr = models.CharField(blank=True, default="", max_length=200)

    def __str__(self):
        return str(self.name) + " " + str(self.count) + " " + str(self.measure)


class AllDescription(models.Model):
    """
    Description
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True)
    step = models.CharField(blank=True, max_length=200)
    photo = models.ImageField(blank=True, upload_to='files/')

    def __str__(self):
        return str(self.step[:100])
