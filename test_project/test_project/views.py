from django.http import HttpResponse

def home(requst):
    return HttpResponse("This is home page ...")
def contuct(requst):
    return HttpResponse("This is contuct page")