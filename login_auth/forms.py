from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=30, required=False,
                                 help_text='Ваше имя. Заполнять не обязательно.')
    last_name = forms.CharField(label="Фамилия", max_length=30, required=False,
                                help_text='Ваша фамилия. Заполнять не обязательно.')
    password1 = forms.CharField(label="Пароль", required=False, widget=forms.PasswordInput, help_text="Введите пароль.")
    password2 = forms.CharField(label="Введите пароль еще раз", required=False, widget=forms.PasswordInput,
                                help_text="Введите пароль еще раз.")

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class AdminUserChangeForm(UserChangeForm):
    first_name = forms.CharField(label="Имя", max_length=30, required=False,
                                 help_text='Ваше имя. Заполнять не обязательно.')
    last_name = forms.CharField(label="Фамилия", max_length=30, required=False,
                                help_text='Ваша фамилия. Заполнять не обязательно.')
    password1 = forms.CharField(label="Пароль", required=False, widget=forms.PasswordInput, help_text="Введите пароль.")
    password2 = forms.CharField(label="Введите пароль еще раз", required=False, widget=forms.PasswordInput,
                                help_text="Введите пароль еще раз.")
    password = None

    class Meta:
        model = User
        # 'username',
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Пароли не совпадают",
                code='password_mismatch',
            )
        return password2

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
