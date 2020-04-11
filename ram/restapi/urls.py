from django.urls import path
# from .views import *
from . import views
from rest_framework.authtoken import views as rview


urlpatterns = [
    path('teacher_profile/', views.TeacherView, name='restapi.tprofile'),
    path('class_history/', views.ClassHistory, name='restapi.history'),
    path('student_wise/', views.StudentHistory, name='restapi.student'),
    path('images_upload/', views.getImage, name='restapi.image'),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'), 
]