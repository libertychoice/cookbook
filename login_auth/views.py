from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import generic

from cookbook.models import Recipe
from login_auth.models import User
from . import forms
from .constants import LOGIN_ERROR


class CreateUserView(generic.View):
    """
    Register new user
    """

    def get(self, request, **kwargs):
        form = forms.SignUpForm()
        return render(request, 'login_auth/register.html', {'form': form})

    def post(self, request, **kwargs):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            new_user = auth.authenticate(username=form.cleaned_data['username'],
                                         password=form.cleaned_data['password2'])

            auth.login(request, new_user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'login_auth/register.html', {'form': form})


class LoginView(generic.View):
    """
    Login
    """

    def get(self, request, **kwargs):
        context = {}
        redirect_url = "/" if not request.GET.get('next') else request.GET.get('next')
        context.update({'next': redirect_url})
        return render(request, 'login_auth/login.html', context)

    def post(self, request, **kwargs):
        redirect_url = "/"
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            else:
                return redirect(redirect_url)
        else:
            login_error = LOGIN_ERROR
            context = {"login_error": login_error}
            return render(request, 'login_auth/login.html', context)


class LogoutView(generic.RedirectView):
    """
    Logout
    """

    def get(self, request, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect("/")


class ShowUserView(generic.View):
    """
    Show user information
    """

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        recipes = sorted(Recipe.objects.filter(author=user_id), key=lambda x: x.id)
        form = forms.AdminUserChangeForm(instance=user)
        return render(request, 'login_auth/user.html', {'form': form, 'recipes': recipes})


class ChangeUserView(generic.View):
    """
    Change user params
    """

    def get_user_recipes(self, user_id):
        """
        Get recipes, created by selected user
        :param user_id:
        :return: user object, recipes
        """

        user = get_object_or_404(User, id=user_id)
        recipes = sorted(get_list_or_404(Recipe, author=user_id), key=lambda x: x.id)
        return user, recipes

    def get(self, request, user_id):
        user, recipes = self.get_user_recipes(user_id)
        form = forms.AdminUserChangeForm(instance=user)
        return render(request, 'login_auth/user.html', {'form': form, 'recipes': recipes})

    def post(self, request, user_id):
        user, recipes = self.get_user_recipes(user_id)
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        form = forms.AdminUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            if password1 and password2:
                user.set_password(password2)
                user.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'login_auth/user.html', {'form': form, 'recipes': recipes})
