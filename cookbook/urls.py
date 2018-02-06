from dal import autocomplete
from taggit.models import Tag
from .models import Ingredient

from django.urls import include, path
from . import views

choices = []
for i in Ingredient.objects.all():
    choices.append(Tag(name=i.name))


def get_ingredients():
    # return [Tag(name="test1"),Tag(name="test2")]
    return choices

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('category/<int:category_id>/', views.show_category, name='show_category'),
    path('recipes/<int:recipe_id>/', views.show_recipe, name='recipe_page'),
    path(
        'test-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=get_ingredients(),
        ),
        name='select2_list',
    ),
]

# path('search_recipe/', views.search_recipe, name='search_recipe'),
# path('create/', views.create, name='create'),
# path('recipes/', views.recipes, name='recipes'),
