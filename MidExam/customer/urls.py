from django.urls import path 

from . import views 

urlpatterns = [
    
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',views.CreateLoginView.as_view(),name='login'),
    path('logout/',views.CreateLogOut.as_view(),name='logout'),
    path('profile/',views.CreateProfileView,name='profile'),
]
