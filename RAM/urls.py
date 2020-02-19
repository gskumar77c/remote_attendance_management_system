from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'RAM-home'),
    path('courses/',views.courses,name = 'RAM-courses'),
    path('login/',views.login)
]