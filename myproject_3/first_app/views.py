from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'author' : 'Rahim', 'age': 20, 'li st': [1,2,3]}
    return render(request, 'home.html', d)
