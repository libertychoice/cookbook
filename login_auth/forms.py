from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from .constants import USER_NAME, USER_NAME_HELP_TEXT, LAST_NAME, \
    LAST_NAME_HELP_TEXT, PASSWD1, PASSWD1_HELP_TEXT, \
    PASSWD2, PASSWD2_HELP_TEXT, VALIDATION_ERROR


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label=USER_NAME, max_length=30, required=False,
                                 help_text=USER_NAME_HELP_TEXT)
    last_name = forms.CharField(label=LAST_NAME, max_length=30, required=False,
                                help_text=LAST_NAME_HELP_TEXT)
    password1 = forms.CharField(label=PASSWD1, required=False, widget=forms.PasswordInput, help_text=PASSWD1_HELP_TEXT)
    password2 = forms.CharField(label=PASSWD2, required=False, widget=forms.PasswordInput,
                                help_text=PASSWD2_HELP_TEXT)

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
    first_name = forms.CharField(label=USER_NAME, max_length=30, required=False,
                                 help_text=USER_NAME_HELP_TEXT)
    last_name = forms.CharField(label=LAST_NAME, max_length=30, required=False,
                                help_text=LAST_NAME_HELP_TEXT)
    password1 = forms.CharField(label=PASSWD1, required=False, widget=forms.PasswordInput, help_text=PASSWD1_HELP_TEXT)
    password2 = forms.CharField(label=PASSWD2, required=False, widget=forms.PasswordInput,
                                help_text=PASSWD2_HELP_TEXT)
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                VALIDATION_ERROR,
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
