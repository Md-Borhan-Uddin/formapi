from django.shortcuts import render
from . forms import UserCreateForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data['last_name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['password1'])
            print(form.cleaned_data['password2'])
    else:
        form = UserCreateForm()
    context = {'form':form}
    return render(request, 'home.html', context)