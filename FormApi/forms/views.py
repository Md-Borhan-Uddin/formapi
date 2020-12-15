from django.shortcuts import render
from .forms import UserCreateForm

# Create your views here.
def formViews(request):
    form = UserCreateForm(auto_id='n_%s',label_suffix=' ')
    context = {'form':form}
    return render(request, 'forms/forms.html', context)