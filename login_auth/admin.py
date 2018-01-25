from django.contrib import admin
# from .forms import AdminUserChangeForm, SignUpForm
from .models import User
from .forms import SignUpForm
from django.contrib.auth import admin as auth_admin
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.utils.translation import ugettext_lazy as _
#
#
# class UserAdmin(BaseUserAdmin):
#     form = AdminUserChangeForm
#     add_form = SignUpForm
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': (
#             'first_name',
#             'last_name',
#             'email'
#         )}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2')}
#          ),
#     )
#
#
# admin.site.register(User, UserAdmin)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = SignUpForm


admin.site.register(User, MyUserAdmin)