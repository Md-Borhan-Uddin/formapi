from django.shortcuts import render
from .forms import UserCreateForm

# Create your views here.
def formViews(request):
    form = UserCreateForm()
    context = {'form':form}
    return render(request, 'forms/forms.html', context)