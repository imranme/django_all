from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

from car.models import CarModel

class SignupView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name="common_form.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Sign Up'
        return context

class CreateLoginView(LoginView):
    template_name='common_form.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Log In'
        return context

    def form_valid(self,form):
        messages.success(self.request,'Login successful')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'Invalid login')
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
    
@method_decorator(login_required,name='dispatch')
class CreateLogOut(generic.View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
@login_required
def  CreateProfileView(request):
    data=CarModel.objects.filter(customer=request.user)
    return render(request,'customer_profile.html',{'data':data})




