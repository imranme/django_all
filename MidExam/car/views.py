from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . models  import CarModel
from brand.models import BrandModel
# Create your views here.




