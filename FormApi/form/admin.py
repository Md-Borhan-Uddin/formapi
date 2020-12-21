from django.contrib import admin
from .models import Persen
# Register your models here.
@admin.register(Persen)

class PersionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'password']