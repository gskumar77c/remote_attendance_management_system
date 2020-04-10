from django.urls import path
from . import views

urlpatterns = [

    path("login",views.login,name="profiles.login"),
    # path("logout",views.logout),
    path("register",views.register,name="profiles.register"),
    # path("update", views.update)
    path('dashboard',views.dashboard,name="profiles.dashboard"),
    path('logout',views.logout,name="profiles.logout")
]
