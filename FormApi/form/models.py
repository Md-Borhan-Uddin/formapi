from django.db import models
from django.core.exceptions import ValidationError


 
# Create your models here.
class Persen(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    def clean_name(name):
        cleaned_data = super().clean()
        if len(name) > 6:
            raise ValidationError('must be 6 char')
        return name