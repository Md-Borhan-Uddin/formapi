from django import forms

class UserCreateForm(forms.Form):
    username = forms.CharField(min_length=7, error_messages={'required':'must 7 char'})
    email = forms.EmailField(min_length=10)
    password = forms.CharField()
    password2 = forms.CharField()
    
    
    def clean_username(self):
        name = self.cleaned_data.get('username')
        if len(name) > 8:
            raise forms.ValidationError('not valid name')
        return name
        
    def clean_password(self):
        pas = self.cleaned_data.get('password')
        if len(pas) < 4:
            raise forms.ValidationError('too short')
        return pas
        
        
    def clean(self):
        cleaned_data = super().clean()
        pas1 = self.cleaned_data.get('password')
        pas2 = self.cleaned_data.get('password2')
        if pas1 != pas2:
            raise forms.ValidationError('password not match')
        
    