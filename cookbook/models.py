from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.
MAX_LEN_TEXT = 20

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
    (1, "Кг"),
    (2, "Граммы")
)

TIME_CHOICES = (
    ("Минуты", "Минуты"),
    ("Часы", "Часы")
)


class CategoryUsing(models.Model):
    # options = models.IntegerField(choices=CATEGORY_USING_CHOICES, blank=True)
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options
        # return list(filter(lambda x: x[0] == self.options, CATEGORY_USING_CHOICES))[0][1]


class CategoryGeo(models.Model):
    # options = models.IntegerField(choices=CATEGORY_GEO_CHOICES, blank=True)
    #
    # def __str__(self):
    #     return list(filter(lambda x: x[0] == self.options, CATEGORY_GEO_CHOICES))[0][1]
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryMain(models.Model):
    # options = models.IntegerField(choices=CATEGORY_MAIN_CHOICES, blank=True)
    #
    # def __str__(self):
    #     return list(filter(lambda x: x[0] == self.options, CATEGORY_MAIN_CHOICES))[0][1]
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryDiet(models.Model):
    # options = models.IntegerField(choices=CATEGORY_DIET_CHOICES, blank=True)
    #
    # def __str__(self):
    #     return list(filter(lambda x: x[0] == self.options, CATEGORY_DIET_CHOICES))[0][1]
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


class CategoryCooking(models.Model):
    # options = models.IntegerField(choices=CATEGORY_COOKING_CHOICES, blank=True)
    #
    # def __str__(self):
    #     return list(filter(lambda x: x[0] == self.options, CATEGORY_COOKING_CHOICES))[0][1]
    #
    options = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.options


# class Time(models.Model):
#     time = models.CharField(max_length=200)
#     measure = models.IntegerField(choices=TIME_CHOICES)
#


def get_path(instance, filename):
    return 'recipes/{}/files/{}'.format(instance.pk, filename)


class Recipe(models.Model):
    """
    Recipe model
    """
    # id = models.PositiveIntegerField(verbose_name="Номер")
    recipe_name = models.CharField(blank=True, max_length=200)
    shortdescription = models.CharField(blank=True, max_length=200)
    youtube = models.CharField(blank=True, help_text="Вставьте ссылку на видео с YouTube, если она имеется",
                               max_length=200)
    # category_using = models.CharField(max_length=200)
    category_using = models.ManyToManyField(CategoryUsing, blank=True)
    # category_using = models.ForeignKey(CategoryUsing,  on_delete=models.CASCADE, default="")
    category_geo = models.ManyToManyField(CategoryGeo, blank=True)
    category_main = models.ManyToManyField(CategoryMain, blank=True)
    category_diet = models.ManyToManyField(CategoryDiet, blank=True)
    category_cooking = models.ManyToManyField(CategoryCooking, blank=True)
    # ingredients = models.ManyToManyField(Ingredient, blank=True)
    time = models.CharField(blank=True, max_length=200)
    measure = models.CharField(blank=True, max_length=200, choices=TIME_CHOICES)
    # description = models.ManyToManyField(AllDescription, blank=True)
    alldescr = models.TextField(blank=True, max_length=200)
    count = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True)
    #,upload_to = 'files/'
    # datetime = models.DateTimeField(auto_now=True)
    # author = models.TextField(blank=True,)
    # calories = models.TextField(blank=True,)

    def __str__(self):
        return self.recipe_name

    def get_short_text(self):
        if len(self.shortdescription) > 10:
            return self.shortdescription[:MAX_LEN_TEXT]
        else:
            return self.shortdescription


@receiver(pre_save, sender=Recipe)
def replace_youtube_link(sender, instance, **kwargs):
    instance.youtube = instance.youtube.replace("youtu.be", "www.youtube.com/embed")


class Ingredient(models.Model):
    """
    Ingredient with description
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True)
    name = models.CharField(blank=True, max_length=200)
    count = models.IntegerField(blank=True, default=1)
    measure = models.IntegerField(blank=True, choices=MEASURE_CHOICES)
    ingr_descr = models.CharField(blank=True, default="", max_length=200)

    def __str__(self):
        return str(self.name) + " " + str(self.count) + " " + str(
            list(filter(lambda x: x[0] == self.measure, MEASURE_CHOICES))[0][1])


class AllDescription(models.Model):
    """
    Description
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True)
    step = models.CharField(blank=True, max_length=200)
    photo = models.ImageField(blank=True, upload_to='files/')

    # uploads/%Y/%m/%d/
    def __str__(self):
        return str(self.step[:100])
