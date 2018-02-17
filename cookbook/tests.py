from django.test import TestCase
from django.urls import reverse
from .forms import *
from .models import *


class RecipeFormTest(TestCase):

    def test_RecipeForm_valid(self):
        form = RecipeForm(data={'recipe_name': "Test Recipe", 'shortdescription': "Simple description",
                                'count': 5, 'time': 40, 'measure': "минут"})
        self.assertTrue(form.is_valid())

    def test_RecipeForm_invalid(self):
        form = RecipeForm(data={'shortdescription': "Simple description",
                                'count': "5", 'time': 40, 'measure': "минут"})

        self.assertFalse(form.is_valid())


class SetUp(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="test@test.ru", password1="12345678i.", password2="12345678i.")
        self.recipe = Recipe.objects.create(recipe_name="Test Recipe", shortdescription="Simple description", count=3,
                                            time=10,
                                            measure="минут", author_id=self.user.id)


class RecipeViewTest(SetUp):

    def test_show_recipe_view(self):
        response = self.client.get(reverse('recipe_page', kwargs={'recipe_id': self.recipe.id}))
        self.assertEqual(response.status_code, 200)

    def test_show_invalid_recipe_view(self):
        response = self.client.get(reverse('recipe_page', kwargs={'recipe_id': self.recipe.id}))
        self.assertEqual(response.status_code, 200)

