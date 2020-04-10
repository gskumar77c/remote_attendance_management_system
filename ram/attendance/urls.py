from django.urls import path,include
from . import views

urlpatterns=[

    path('',views.home,name="attendance.home"),
    path('new_entry', views.web_input,name="attendance.new_entry"),
    path('history',views.history_courses,name="attendance.history_courses"),
    path('history/<pk>', views.history,name="attendance.history"),
    path('details/<int:pk>',views.details,name="attendance.details"),
    path('modify/<int:pk>',views.modify,name="attendance.modify"),

]