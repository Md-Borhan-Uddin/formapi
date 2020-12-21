from django.shortcuts import render
from . forms import PersenCreateForm
from .models import Persen

# Create your views here.
def home(request):
    pn = Persen.objects.get(id=1)
    if request.method == "POST":
        form = PersenCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            ps = form.cleaned_data['password']
            
            person = Persen(name=name, email=email, password=ps)
            person.save()
            
    else:
        form = PersenCreateForm()
    context = {'form':form}
    return render(request, 'home.html', context)