from django.urls import path
from institution import views

urlpatterns = [
    path('', views.home),
    path('slot_init',views.create_slots)
]
