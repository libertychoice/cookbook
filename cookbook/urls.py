from dal import autocomplete
from taggit.models import Tag
from .models import Ingredient
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from . import views

choices = []
for i in Ingredient.objects.all():
    choices.append(Tag(name=i.name))


def get_ingredients():
    return choices


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('create_recipe/', login_required(views.CreateRecipeView.as_view()), name='create_recipe'),
    path('category/<int:category_id>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('recipes/<int:recipe_id>/', views.ShowRecipeView.as_view(), name='recipe_page'),
    path(
        'test-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(
            queryset=get_ingredients(),
        ),
        name='select2_list',
    ),
]

