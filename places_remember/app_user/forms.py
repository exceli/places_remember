from allauth.account.forms import LoginForm
from django import forms


class CustomLoginForm(LoginForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-controls'})
    )
    passwords = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )