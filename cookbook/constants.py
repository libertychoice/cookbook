"""
Constants for application
"""

RECIPE_NAME = "Название рецепта"
DESCRIPTION = "Описание"
YOUTUBE = "Видео с YouTube"
YOUTUBE_HELP = "Вставьте ссылку на видео с YouTube, если она имеется"
CATEGORY_USING = "Назначение"
CATEGORY_GEO = "География кухни"
CATEGORY_MAIN = "Блюдо"
CATEGORY_DIET = "Диета"
CATEGORY_COOKING = "Приготовление"
ALL_DESCR = "Текст рецепта"
COUNT = "Количество порций"
TIME = "Время приготовления"
AUTHOR = "Автор рецепта"
INGREDIENTS = "Ингридиенты"
DATE_TIME = "Дата создания"

CATEGORY_USING_CHOICES = (
    ("1", "На обед"),
    ("2", "На завтрак")
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

MAX_LEN_TEXT = 200
UPLOAD_PHOTO_DIR = "files/"

HOME_TITLE = "Свежие рецепты"
FILTER_TITLE = "Найденные рецепты"
