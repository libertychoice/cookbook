from django import forms
from . import models
from djangoformsetjs.utils import formset_media_js

RECIPE_NAME = "Название рецепта"
DESCRIPTION = "Описание"
YOUTUBE = "Видео с YouTube"
CATEGORY_USING = "Назначение"
CATEGORY_GEO = "География кухни"
CATEGORY_MAIN = "Блюдо"
CATEGORY_DIET = "Диета"
CATEGORY_COOKING = "Приготовление"
ALL_DESCR = "Текст рецепта"
COUNT = "Количество порций"
TIME = "Время приготовления"
AUTHOR = "Автор рецепта"

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


class IngredientForm(forms.ModelForm):
    recipe = forms.ModelChoiceField(required=False, queryset=models.Recipe.objects.all())
    name = forms.CharField(required=False, max_length=200)
    count = forms.IntegerField(required=False, widget=forms.TextInput)
    measure = forms.ChoiceField(required=False, choices=MEASURE_CHOICES)
    ingr_descr = forms.CharField(required=False, widget=forms.Textarea, max_length=200)

    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'ingr1'})
        self.fields['count'].widget.attrs.update({'class': 'ingr1'})
        self.fields['ingr_descr'].widget.attrs.update({'class': 'form-control autosize', 'rows': '1'})

    class Media(object):
        js = formset_media_js + (
            # Other form media here
        )

    class Meta:
        model = models.Ingredient
        fields = '__all__'


class AllDescriptionForm(forms.ModelForm):
    step = forms.CharField(required=False, widget=forms.Textarea, max_length=200)
    photo = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(AllDescriptionForm, self).__init__(*args, **kwargs)
        self.fields['step'].widget.attrs.update({'class': 'form-control autosize', 'rows': '1'})

    class Media(object):
        js = formset_media_js + (
            # Other form media here
        )

    class Meta:
        model = models.AllDescription
        fields = '__all__'




class RecipeForm(forms.ModelForm):
    recipe_name = forms.CharField(label=RECIPE_NAME, max_length=100)
    shortdescription = forms.CharField(label=DESCRIPTION, required=False, widget=forms.Textarea, max_length=200)
    youtube = forms.CharField(label=YOUTUBE, required=False, max_length=100)
    category_using = forms.MultipleChoiceField(label=CATEGORY_USING, required=False, widget=forms.CheckboxSelectMultiple,
                                               choices=models.CategoryUsing.objects.all().values_list('id', 'options'))
    category_geo = forms.MultipleChoiceField(label=CATEGORY_GEO, required=False,
                                             widget=forms.CheckboxSelectMultiple,
                                             choices=models.CategoryGeo.objects.all().values_list('id', 'options'))
    category_main = forms.MultipleChoiceField(label=CATEGORY_MAIN, required=False, widget=forms.CheckboxSelectMultiple,
                                              choices=models.CategoryMain.objects.all().values_list('id', 'options'))
    category_diet = forms.MultipleChoiceField(label=CATEGORY_DIET, required=False, widget=forms.CheckboxSelectMultiple,
                                              choices=models.CategoryDiet.objects.all().values_list('id', 'options'))
    category_cooking = forms.MultipleChoiceField(label=CATEGORY_COOKING, required=False,
                                                 widget=forms.CheckboxSelectMultiple,
                                                 choices=models.CategoryCooking.objects.all().values_list('id',
                                                                                                          'options'))
    alldescr = forms.CharField(label=ALL_DESCR, widget=forms.Textarea, required=False, max_length=1000)
    count = forms.CharField(label=COUNT, required=True, max_length=5)
    time = forms.CharField(label=TIME, required=False, max_length=200)
    measure = forms.ChoiceField(required=False, choices=TIME_CHOICES)
    image = forms.ImageField(required=False)
    author = forms.CharField(label=AUTHOR, required=False, max_length=200)


    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['recipe_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['shortdescription'].widget.attrs.update({'class': 'form-control autosize', 'rows': '1'})
        self.fields['youtube'].widget.attrs.update({'class': 'form-control'})
        self.fields['alldescr'].widget.attrs.update({'class': 'form-control autosize', 'rows': '1'})

    class Meta:
        model = models.Recipe
        fields = '__all__'
