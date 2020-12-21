from django.shortcuts import render
from .forms import UserCreateForm
from . models import User
# Create your views here.
def formViews(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = User(username=name, emasil=email, password=password)
            reg.save()
    else:        
        form = UserCreateForm(label_suffix=' ')
    context = {'form':form}
    return render(request, 'forms/forms.html', context)