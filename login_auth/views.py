from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf

from cookbook.models import Recipe, Ingredient, AllDescription
from django.forms.formsets import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext, loader, Template
from django.contrib import auth

from login_auth.models import User
from . import forms
import json

LOGIN_ERROR = "Пользователь не существует"

def create_user(request):
    """
    Register new user
    :param request:
    :return:
    """

    #print(str(form))
    form = None
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        # form = UserCreationForm(request.POST)

        if form.is_valid():
            recipe = form.save()
            # new_user = auth.authenticate(username=form.cleaned_data['username'],
            #
            #                             password=form.cleaned_data['password2'])
            new_user = auth.authenticate(email=form.cleaned_data['username'],

                                         password=form.cleaned_data['password2'])

            auth.login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = forms.SignUpForm()
    print(str(form.error_messages))
    return render(request, 'login_auth/register.html', {'form': form})


def login(request):
    """
    Login
    :param request:
    :return:
    """
    context = {}
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            #t = Template("<button>Make me happy</button>")
            #return t.render(RequestContext(request, {}))
            #return HttpResponseRedirect("/")
            # context.update(csrf(request))
            #print(request.POST)
            return HttpResponseRedirect("/")
            #return render(request, 'login_auth/login.html', context)
        else:
            login_error = LOGIN_ERROR
            context = {"login_error": login_error}
            return render(request, 'login_auth/login.html', context)
    return render(request, 'login_auth/login.html', context)


def logout(request):
    """
    Logout
    :param request:
    :return:
    """
    auth.logout(request)
    return HttpResponseRedirect("/")


def show_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # ingr = sorted(get_list_or_404(Ingredient, recipe=recipe), key=lambda x: x.id)
    # descr = sorted(get_list_or_404(AllDescription, recipe=recipe), key=lambda x: x.id)
    # form = forms.UserChangeForm(instance=user)
    form = forms.AdminUserChangeForm(instance=user)
    return render(request, 'login_auth/user.html', {'form': form, })
