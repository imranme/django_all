"""
URL configuration for MidExam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
from . import views 

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    # path('signup/',views.SignUpView.as_view(),name='signup'),
    # path('login/',views.CreateLoginView.as_view(),name='login'),
    # path('logout/',views.CreateLogout.as_view(),name='logout'),
    path('car/',include('car.urls')),
    path('brand/',include('brand.urls')),
    path('customer/',include('customer.urls')),
    path('brand/<slug:brand_slug>/',views.home,name='brand_wise_car'),
    path('details/<int:id>/',views.ViewDetails.as_view(),name='details'),
    path('car/buy_now/<int:id>/', views.buy_now, name='buy_now'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)