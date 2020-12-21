from django import forms
from .models import Persen

class PersenCreateForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, label='Re-Type Password', widget=forms.PasswordInput())
    class Meta:
        model = Persen
        fields = '__all__'
        labels = {'name':'Username'}
        widgets = {'password':forms.PasswordInput(attrs={'class':'p_name', 'id':'p_id'})}
        # error_messages = {
        #     'name':{
        #         'required':'Emter your name',
        #     },
        # }
            
        # error_messages = {
        #     'name': {
        #         'required': "This is a custom error message from modelform meta",
        #     },
        # }    
        
        def clean(self):
            cleaned_data = super().clean()
            n = self.cleaned_data.get('name')
            print(n)
            if len(n) < 6:
                raise forms.ValidationError('must be 6 char')
            
        