from django.shortcuts import render
from . forms import UserCreateForm
# Create your views here.
def home(request):
    form = UserCreateForm(label_suffix='', initial={'first_name':'Borhan', 'last-name':'setu'}, auto_id='saame')
    context = {'form':form}
    return render(request, 'home.html', context)