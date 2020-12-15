from django import forms


class UserCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100, help_text ='must be 6 charecrture')
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, required=False)
    
    