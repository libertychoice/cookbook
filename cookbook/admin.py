from django.contrib import admin

# Register your models here.
from cookbook.models import *


class IngedientAdmin(admin.TabularInline):
    model = Ingredient


class DescriptionAdmin(admin.TabularInline):
    model = AllDescription


class RecipeAdmin(admin.ModelAdmin):
    # fields = ('recipe_name', 'shortdescription' ,'youtube', 'category_using','category_geo','category_main',
    #         'category_diet','category_cooking','time','measure', 'alldescr','count','image', 'datetime')
    # readonly_fields = ('recipe_name', )
    inlines = [IngedientAdmin, DescriptionAdmin, ]


# admin.site.register([Recipe, CategoryUsing, CategoryGeo, CategoryCooking, CategoryDiet, CategoryMain, AllDescription], RecipeAdmin)
admin.site.register([Recipe, ], RecipeAdmin)
# admin.site.register(AllDescription, DescriptionAdmin)
# admin.site.register(Ingredient, IngedientAdmin)
admin.site.register(CategoryMain)
admin.site.register(CategoryUsing)
admin.site.register(CategoryGeo)
admin.site.register(CategoryCooking)
admin.site.register(CategoryDiet)
