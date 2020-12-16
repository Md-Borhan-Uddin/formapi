from django import forms

class UserCreateForm(forms.Form):
    username = forms.CharField(min_length=7)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        pas1 = self.cleaned_data['password']
        pas2 = self.cleaned_data['password2']
        
        if pas1 != pas2:
            raise forms.ValidationError('password not match')
        
    