from django.shortcuts import render
from .forms import UserForm
from .models import Person

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            person = Person(name=name, email=email, password=password)
            person.save()
    else:
        form = UserForm(label_suffix="")
    context = {'form':form}
    return render(request, 'home.html', context)