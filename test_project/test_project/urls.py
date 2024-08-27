
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("contuct/", views.contuct),
    path("test_app/", include("test_app.urls")),

]
