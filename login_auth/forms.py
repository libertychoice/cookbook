from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=30, required=False,
                                 help_text='Ваше имя. Заполнять не обязательно.')
    last_name = forms.CharField(label="Фамилия", max_length=30, required=False,
                                help_text='Ваша фамилия. Заполнять не обязательно.')
    password1 = forms.CharField(label="Пароль",  widget=forms.PasswordInput, help_text="Введите пароль.")
    password2 = forms.CharField(label="Введите пароль еще раз",  widget=forms.PasswordInput,
                                help_text="Введите пароль еще раз.")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class AdminUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        # 'username',
        fields = ('first_name', 'last_name', 'email')
