from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class UserEditForm(UserChangeForm):
    # first_name = forms.CharField(max_length=100)
    password = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserForm(UserCreationForm):
    # first_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields = '__all__'
        
        help_texts = {
            'username':'must be fill this field',
            'password1':'deedd',
        }
        widgets = {
            'last_name':forms.TextInput(attrs={
                'class':'customclass'
            })
        }
        
        
    # def clean_first_name(self, *args, **kwargs):
    
    #     name = self.cleaned_data.get('first_name')
        
    #     if len(name) < 4:
    #         raise forms.ValidationError('short')
    #     return name