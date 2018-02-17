from django.contrib import admin

from cookbook.models import *


class IngedientAdmin(admin.TabularInline):
    model = Ingredient


class DescriptionAdmin(admin.TabularInline):
    model = AllDescription


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngedientAdmin, DescriptionAdmin, ]


admin.site.register([Recipe, ], RecipeAdmin)
admin.site.register(CategoryMain)
admin.site.register(CategoryUsing)
admin.site.register(CategoryGeo)
admin.site.register(CategoryCooking)
admin.site.register(CategoryDiet)
admin.site.register(RecipeSearchModel)
