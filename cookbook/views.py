from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from cookbook.models import *
from django.forms.formsets import formset_factory
from django.contrib import auth
from django.views import generic
from . import forms

HOME_TITLE = "Свежие рецепты"

# Create your views here.


class UpdateView(generic.UpdateView):
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
        form = forms.RecipeSearchForm(request.POST)
        filter_recipes = get_list_or_404(Recipe, recipe_name__icontains=request.POST['recipe_name'])
        return render(request, 'cookbook/home.html', {'filter_recipes': filter_recipes, 'form': form})


def recipes(request):
    """
    Show index page information
    :param request:
    :return:
    """
    recipes = Recipe.objects.all().order_by('-id')[:10]
    category_main = CategoryMain.objects.all()
    category_using = CategoryUsing.objects.all()
    category_cooking = CategoryCooking.objects.all()
    category_diet = CategoryDiet.objects.all()
    category_geo = CategoryGeo.objects.all()
    username = auth.get_user(request)
    search_form = forms.RecipeSearchForm()
    context = {
        'recipes': recipes,
        'username': username,
        'title': HOME_TITLE,
        'category_main': category_main,
        'category_using': category_using,
        'category_cooking': category_cooking,
        'category_diet': category_diet,
        'category_geo': category_geo,
        'search_form': search_form
    }
    return render(request, 'cookbook/home.html', context)


def about(request):
    return render(request, 'cookbook/about.html')


def create(request):
    return render(request, 'cookbook/create.html')


@login_required
def create_recipe(request):
    """
    Create new recipe
    :param request:
    :return:
    """
    IngrFormSet = formset_factory(forms.IngredientForm, can_delete=True)
    AllDescrFormSet = formset_factory(forms.AllDescriptionForm, can_delete=True)

    if request.method == 'POST':
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
    else:
        ingr = IngrFormSet()
        descr = AllDescrFormSet()
        form = forms.RecipeForm()
    return render(request, 'cookbook/create.html', {'form': form, 'formset': ingr, 'all_descr': descr})


def show_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingr = sorted(get_list_or_404(Ingredient, recipe=recipe), key=lambda x: x.id)
    descr = sorted(AllDescription.objects.filter(recipe=recipe), key=lambda x: x.id)
    form = forms.RecipeForm(instance=recipe)
    return render(request, 'cookbook/recipe.html', {'form': form, 'recipe': recipe, 'ingr': ingr, 'descr': descr})


def show_category(request, category_id):
    category_recipes = Recipe.objects.filter(category_main=category_id)
    return render(request, 'cookbook/category.html', {'category_recipes': category_recipes, })


def search_recipe(request):
    if request.method == 'POST':
        filter_recipes = get_list_or_404(Recipe, recipe_name__icontains=request.POST['recipe_name'])

    return render(request, 'cookbook/home.html', {'category_recipes': {}})
