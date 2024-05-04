from django.shortcuts import render

# /home/tushar/django/myproject2/templates
def index(request):
    return render(request, 'index.html')