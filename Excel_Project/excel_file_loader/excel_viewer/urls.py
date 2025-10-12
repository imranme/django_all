from django.urls import path
from . import views

# URL namespace for the excel_viewer app
app_name = 'excel_viewer'

urlpatterns = [
    # Home page
    path('', views.home_view, name='home'),
    
    # Upload Excel files page
    path('upload/', views.upload_excel_files, name='upload'),
    
    # Display Excel data page
    path('show-data/', views.show_excel_data, name='show_data'),
    
    # Clear session data
    path('clear-session/', views.clear_session_data, name='clear_session'),
]