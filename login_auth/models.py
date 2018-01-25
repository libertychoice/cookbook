from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import models as auth_models

EMAIL_LABEL = "Электронная почта"
EMAIL_HELP_TEXT = "Существующий адрес электронной почты. Все почтовые сообщения с сайта будут отсылаться на этот адрес."


class User(AbstractUser):
    username = models.EmailField(_(EMAIL_LABEL), unique=True, help_text=EMAIL_HELP_TEXT)
    password1 = models.CharField(default="", max_length=200, blank=False)
    password2 = models.CharField(default="", max_length=200, blank=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


