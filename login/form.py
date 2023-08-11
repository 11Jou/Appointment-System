from django import forms
import uuid


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'username'}) , required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}) , required=True)


