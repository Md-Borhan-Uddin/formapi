from django import forms
from . models import Person

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'password':forms.PasswordInput()
        }
        error_messages = {
            'name':{
                'required':'must be attest this field'
            }
        }
        help_texts = {
            'name':'must be 6 char'
        }
    