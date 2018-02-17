from django.test import TestCase
from django.urls import reverse

from login_auth.models import User


class SetUp(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="test@test.com")
        self.user.set_password("12345678i.")
        self.user.save()


class CreateUserViewTest(TestCase):

    def test_create_user_view(self):
        response = self.client.post(reverse('create_user'),
                                    {'username': "test@test.com", "password1": "12345678i.",
                                     "password2": "12345678i."})
        self.assertEqual(response.status_code, 302)

    def test_create_user_invalid_view(self):
        response = self.client.post(reverse('create_user'),
                                    {'username': 1234, "password1": "12345678i.",
                                     "password2": "12345678i."})
        self.assertTrue("register_error" in response.context['errors'])


class LoginViewTest(SetUp):

    def test_login_view(self):
        response = self.client.post(reverse('login'),
                                    {'username': "test@test.com", 'password': "12345678i."})
        self.assertEqual(response.status_code, 302)

    def test_login_invalid_view(self):
        response = self.client.post(reverse('login'),
                                    {'username': "test@test.com", "password": "invalid"})
        self.assertTrue("login_error" in response.context)
