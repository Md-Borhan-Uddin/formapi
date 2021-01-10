from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
    