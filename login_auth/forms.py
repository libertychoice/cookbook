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
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     return password2
    #
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.clean_password2())
    #     if commit:
    #         user.save()
    #     return user

    # def clean(self, *args, **kwargs):
    #     print(str("BBB"))
    #     cleaned_data = super(UserCreationForm, self).clean(*args, **kwargs)
    #     #if cleaned_data.has_key('email'):
    #      #   cleaned_data['username'] = self.__generate_username(
    #      #                                               cleaned_data['email'])
    #     print(str(cleaned_data))
    #     return cleaned_data

class AdminUserChangeForm(UserChangeForm):
    first_name = forms.CharField(label="Имя", max_length=30, required=False,
                                 help_text='Ваше имя. Заполнять не обязательно.')
    last_name = forms.CharField(label="Фамилия", max_length=30, required=False,
                                help_text='Ваша фамилия. Заполнять не обязательно.')

    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        # 'username',
        fields = ('first_name', 'last_name', 'username')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs['readonly'] = True
