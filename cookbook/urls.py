from django.urls import include, path
#from django.conf.urls import url
from . import views

urlpatterns = [
   path('', views.recipes, name='home'),
   path('about/', views.about, name='about'),
   path('create/', views.create, name='create'),
   path('recipes/', views.recipes, name='recipes'),
   path('create_recipe/', views.create_recipe, name='create_recipe'),
   path('recipes/<int:recipe_id>/', views.show_recipe, name='recipe_page'),
]
