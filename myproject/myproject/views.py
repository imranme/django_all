from django.http import HttpResponse

def home(requst):
    return HttpResponse("This is Home Page")
def contact(requst):
    return HttpResponse("This is contact page") 