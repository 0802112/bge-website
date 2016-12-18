from django import forms


class UserForm(forms.Form):
    lastname = forms.CharField(max_length=50, widget=forms.TextInput)
    firstname = forms.CharField(max_length=50, widget=forms.TextInput)
    email = forms.EmailField(max_length=100, widget=forms.TextInput)
    username = forms.CharField(max_length=30, widget=forms.TextInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())