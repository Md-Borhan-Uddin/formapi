from django import forms

class UserCreateForm(forms.Form):
    username = forms.CharField(min_length=7)
    email = forms.EmailField(min_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
 
        
    