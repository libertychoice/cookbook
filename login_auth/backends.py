from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

#
# class EmailAuthBackEnd(ModelBackend):
#     def authenticate(self, email=None, password=None,**kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=email)
#             if user.check_password(password):
#                 return user
#             return None
#         except UserModel.DoesNotExist:
#             return None
