from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import UserForm, UserEditForm
# Create your views here.


def singupView(request):
    user = User.objects.get(id=1)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'accounts/singup.html', context)


def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('singup')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def passChangeView(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request, 'accounts/pass_change.html', context)



def profileChangeView(request):
    if request.method == "POST":
        form = UserEditForm()
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserEditForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/profile.html', context)


def logoutView(request):
    pass