from django import forms


class UserCreateForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, initial="Tinne")
    username = forms.CharField(max_length=100,)
    email = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100, label='password')
    password2 = forms.CharField(max_length=100, label='Confirm Passwors')
    
    # def clean_password1(self):
    #     pas1 = self.cleaned_data['password1']
       
    #     if len(pas1)<8:
    #         raise forms.ValidationError('Password too short')
    #         print('Password too short')
    #     return pas1
    
    def clean(self):
        cleaned_data  = super().clean()
        pas1 = self.cleaned_data['password1']
        if len(pas1) < 8:
            raise forms.ValidationError('password too short')            
        