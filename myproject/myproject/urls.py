
from django.contrib import admin
from django.urls import path
# from views import contact
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact)
]
