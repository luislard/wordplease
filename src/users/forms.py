from django import forms


class LoginForm(forms.Form):
    login_username = forms.CharField(label='Username')
    login_password = forms.CharField(widget=forms.PasswordInput(), label='Password')