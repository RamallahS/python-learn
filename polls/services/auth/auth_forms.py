from django import forms


class RegistrationForm(forms.Form):
    email = forms.CharField(max_length=1)
    password = forms.CharField(max_length=1)
