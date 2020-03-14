from django.urls import path
from . import views

urlpatterns = [

    path("login",views.login),
    # path("logout",views.logout),
    path("register",views.register),
    # path("update", views.update)
    path('dashboard',views.dashboard),
    path('logout',views.logout)
]
