from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('register/',views.register,name = 'gsregister'),
    path('student/',views.student_register,name='student_register'),
    path('faculty/',views.faculty_register,name = 'faculty_register'),
    #path('login/',views.login,name='login'),
    path('',auth_views.LoginView.as_view(template_name='authentication/login.html'),name='login')
]
