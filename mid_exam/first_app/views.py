from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def home(request):
    if request.method == 'post':
        form = RegisterForm()
        if form.is_valid():
            form.save(commit=False)
        else:
            form = RegisterForm()
        return render(request, './home.html', {'form': form})