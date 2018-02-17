import operator
from functools import reduce

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import generic

from cookbook.models import *
from . import forms

HOME_TITLE = "Свежие рецепты"
FILTER_TITLE = "Найденные рецепты"

# Create your views here.


class IndexView(generic.UpdateView):
    """
    Show index page information with search form
    """
    model = RecipeSearchModel
    form_class = forms.RecipeSearchForm
    template_name = 'cookbook/home.html'
    title = HOME_TITLE

    def get_recipes(self):
        return Recipe.objects.all().order_by('-id')[:10]

    def get_category_main(self):
        return CategoryMain.objects.all()

    def get_category_using(self):
        return CategoryUsing.objects.all()

    def get_category_cooking(self):
        return CategoryCooking.objects.all()

    def get_category_diet(self):
        return CategoryDiet.objects.all()

    def get_category_geo(self):
        return CategoryGeo.objects.all()

    def get_object(self):
        return Ingredient.objects.first()

    def post(self, request, **kwargs):
        filter_names = ('recipe_name',)
        filter_categories = ('category_diet', 'category_using', 'category_geo', 'category_main', 'category_cooking',)
        filter_ingredients = ('ingredient',)
        filter_names_list = [Q(**{field + '__icontains': request.POST[field]}) for field in filter_names if
                             request.POST.get(field)]
        filter_categories_list = (Q(**{field + '__id': request.POST[field]}) for field in filter_categories if
                                  request.POST.get(field))
        filter_ingredients_list = (Q(**{field + '__name__icontains': request.POST[field]}) for field in
                                   filter_ingredients if
                                   request.POST.get(field))
        filters = list(filter_names_list) + list(filter_categories_list) + list(filter_ingredients_list)
        form = forms.RecipeSearchForm(request.POST)
        filter_recipes = Recipe.objects.filter(reduce(operator.and_, filters))
        # filter_recipes = get_list_or_404(Recipe, recipe_name__icontains=request.POST['recipe_name'])
        return render(request, 'cookbook/home.html',
                      {'filter_recipes': filter_recipes, 'form': form, 'filter_title': FILTER_TITLE})


# def recipes(request):
#     """
#     Show index page information with search form
#     :param request:
#     :return:
#     """
#     recipes = Recipe.objects.all().order_by('-id')[:10]
#     category_main = CategoryMain.objects.all()
#     category_using = CategoryUsing.objects.all()
#     category_cooking = CategoryCooking.objects.all()
#     category_diet = CategoryDiet.objects.all()
#     category_geo = CategoryGeo.objects.all()
#     username = auth.get_user(request)
#     search_form = forms.RecipeSearchForm()
#     context = {
#         'recipes': recipes,
#         'username': username,
#         'title': HOME_TITLE,
#         'category_main': category_main,
#         'category_using': category_using,
#         'category_cooking': category_cooking,
#         'category_diet': category_diet,
#         'category_geo': category_geo,
#         'search_form': search_form
#     }
#     return render(request, 'cookbook/home.html', context)


class AboutView(generic.View):
    """
    Render About page
    """

    def get(self, request, **kwargs):
        return render(request, 'cookbook/about.html')


# def create(request):
#     return render(request, 'cookbook/create.html')


class CreateRecipeView(generic.View):
    """
    Create new recipe
    """
    def get(self, request, **kwargs):
        IngrFormSet = formset_factory(forms.IngredientForm, can_delete=True)
        AllDescrFormSet = formset_factory(forms.AllDescriptionForm, can_delete=True)
        ingr = IngrFormSet()
        descr = AllDescrFormSet()
        form = forms.RecipeForm()
        return render(request, 'cookbook/create.html', {'form': form, 'formset': ingr, 'all_descr': descr})

    def post(self, request, **kwargs):
        IngrFormSet = formset_factory(forms.IngredientForm, can_delete=True)
        AllDescrFormSet = formset_factory(forms.AllDescriptionForm, can_delete=True)
        json_string = request.POST
        form = forms.RecipeForm(request.POST, request.FILES, initial={'author': ""})
        if form.is_valid():

            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            ingr = IngrFormSet(request.POST, request.FILES)
            for i in ingr:
                p = i.save(commit=False)
                p.recipe = recipe
                p.save()
            descr = AllDescrFormSet(request.POST, request.FILES)

            for d in descr:
                p = d.save(commit=False)
                p.recipe = recipe
                p.save()
            return render(request, 'cookbook/added.html', {'form': form, 'recipe': recipe})

def show_recipe(request, recipe_id):
    """
    Get recipe by id
    :param request:
    :param recipe_id:
    :return: Form, Recipe object, Ingredient object, AllDescription object (description with steps)
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingr = sorted(get_list_or_404(Ingredient, recipe=recipe), key=lambda x: x.id)
    descr = sorted(AllDescription.objects.filter(recipe=recipe), key=lambda x: x.id)
    form = forms.RecipeForm(instance=recipe)
    return render(request, 'cookbook/recipe.html', {'form': form, 'recipe': recipe, 'ingr': ingr, 'descr': descr})


def show_category(request, category_id):
    """
    Get recipes by category
    :param request:
    :param category_id:
    :return: Recipe objects filtered by category
    """
    category_recipes = Recipe.objects.filter(category_main=category_id)
    return render(request, 'cookbook/category.html', {'category_recipes': category_recipes, })

# def search_recipe(request):
#     if request.method == 'POST':
#         print(request.POST)
#         filter_recipes = get_list_or_404(Recipe, recipe_name__icontains=request.POST['recipe_name'])
#
#     return render(request, 'cookbook/home.html', {'category_recipes': {}})
