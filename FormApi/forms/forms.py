from django import forms

class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
    
    def clean_password(self):
        password = self.cleaned_data['password']
        
        if len(password) <= 6:
            raise forms.ValidationError('password too short')   
        return password
    
    def clean_username(self):
        name = self.cleaned_data['username']
        
        if len(name) < 5:
            raise forms.ValidationError('username must be 5 characture')
        return name
    