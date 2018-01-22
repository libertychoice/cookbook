from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from cookbook.models import Recipe, Ingredient, AllDescription
from django.forms.formsets import formset_factory
import json
from . import forms


# Create your views here.

def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'cookbook/home.html', context)
    # return HttpResponse('RECIPES')


def about(request):
    return render(request, 'cookbook/about.html')


def create(request):
    return render(request, 'cookbook/create.html')


def create_recipe(request):
    """
    Create new recipe
    :param request:
    :return:
    """
    IngrFormSet = formset_factory(forms.IngredientForm, can_delete=True)
    AllDescrFormSet = formset_factory(forms.AllDescriptionForm, can_delete=True)
    # TimeFormSet = formset_factory(forms.TimeForm, can_delete=True)
    # formset = forms.RecipeForm,

    print(str(request.FILES))
    # time = TimeFormSet()
    # initial=[{'name': "masha", "count": 1, "measure": "кг"}]
    if request.method == 'POST':
        json_string = request.POST
        print(json_string)

        # form_data = json.loads(json_string)[0]
        form = forms.RecipeForm(request.POST, request.FILES)

        if form.is_valid():

            recipe = form.save()
            ingr = IngrFormSet(request.POST, request.FILES)
            for i in ingr:
                p = i.save(commit=False)
                p.recipe = recipe
                p.save()
            descr = AllDescrFormSet(request.POST, request.FILES)
            print(str(descr.errors))
            for d in descr:
                p = d.save(commit=False)
                p.recipe = recipe
                p.save()
            return render(request, 'cookbook/added.html', {'form': form})
    else:
        ingr = IngrFormSet()
        descr = AllDescrFormSet()
        form = forms.RecipeForm()
    # , 'all_descr': descr
    # print(form)
    return render(request, 'cookbook/create.html', {'form': form, 'formset': ingr, 'all_descr': descr})


def show_recipe(request, recipe_id):
    # recipes = Recipe.objects.all().values()

    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingr = sorted(get_list_or_404(Ingredient, recipe=recipe), key=lambda x: x.id)
    descr = sorted(get_list_or_404(AllDescription, recipe=recipe),key=lambda x: x.id)
    form = forms.RecipeForm(instance=recipe)
    print(descr)
    return render(request, 'cookbook/recipe.html', {'form': form, 'recipe': recipe, 'ingr': ingr, 'descr': descr})
