from django import forms


class UserCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, initial="Tinne")
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100, label='password')
    password2 = forms.CharField(max_length=100, label='Confirm Passwors')