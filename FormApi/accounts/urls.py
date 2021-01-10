from django.urls import path
from . import views

urlpatterns = [
    path('', views.singupView, name='singup'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('pass_change', views.passChangeView, name='pass_change'),
    path('edit_profile', views.profileChangeView, name='profile'),
]
