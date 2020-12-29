from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name