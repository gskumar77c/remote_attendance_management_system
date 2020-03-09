from django.urls import path
from institution import views

urlpatterns = [
    path('', views.home),
    
]
