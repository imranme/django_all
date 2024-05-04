
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



from brand.models import BrandModel
from car.models import CarModel
from car.forms import CommentForm


from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST


def home(request,brand_slug=None):

    data=CarModel.objects.all()
    if brand_slug is not None:
        brand=BrandModel.objects.get(slug=brand_slug)
        data=CarModel.objects.filter(BrandName=brand)
    brands=BrandModel.objects.all()
    return render(request, 'home.html',{'data':data, 'brand':brands})


class ViewDetails(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'view_details.html'
    success_url = reverse_lazy('details')

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car_object = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car_object
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_object = self.object 
        comments = car_object.comments.all()
        comment_form = CommentForm()
        context['comment'] = comments
        context['comment_form'] = comment_form
        return context

def buy_now(request, id):
    car_object = get_object_or_404(CarModel, id=id)

    # Reduce the quantity by 1
    if car_object.Quantity > 0:
        car_object.Quantity -= 1
        car_object.save()

    if request.user.is_authenticated:
        request.user.customer.add(car_object)

    return redirect('details', id=id)

   

class SignUpView(generic.CreateView):

    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='common_form.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Sign Up'
        return context

class CreateLoginView(LoginView):
    template_name='common_form.html'
    def form_valid(self,form):
        messages.success(self.request,'Login successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Login failed')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Log In'
        return context

    def get_success_url(self):
        return reverse_lazy('home')
    

@method_decorator(login_required,name='dispatch')
class CreateLogout(generic.View):

    def get(self,request):
        logout(request)
        return redirect('home')


    
    