from django.shortcuts import render
from .forms import UserCreateForm

# Create your views here.
def formViews(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            print('formvalidated')
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name, email, password)
            # print(form.cleaned_data['password'])
    else:        
        form = UserCreateForm(label_suffix=' ')
    context = {'form':form}
    return render(request, 'forms/forms.html', context)