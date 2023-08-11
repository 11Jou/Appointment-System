from django import forms


class CreateUser(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'username', 'autocomplete': 'off'}) , required=True)
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Email' , 'autocomplete':'off'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'autocomplete': 'off'}), required=True)