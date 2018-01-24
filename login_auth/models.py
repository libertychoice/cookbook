from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

EMAIL_LABEL = "Электронная почта"
EMAIL_HELP_TEXT = "Существующий адрес электронной почты. Все почтовые сообщения с сайта будут отсылаться на этот адрес."

class User(AbstractUser):
    username = models.EmailField(_(EMAIL_LABEL), unique=True, help_text=EMAIL_HELP_TEXT)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


