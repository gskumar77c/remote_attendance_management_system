from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home),
    path('new_entry', views.web_input),
    path('history',views.history_courses,name='history-courses'),
    path('history/<pk>', views.history),
    path('details/<int:pk>',views.details),
    path('modify/<int:pk>',views.modify,name='modify-attendance'),
    # path('coursedetails',views.coursedetails,name= 'course-details'),
    # path('floated_courses',views.show_floated_courses,name='floated-courses'),
    # path('add_request',views.send_request,name='add-request'),
    # path('enrolled_courses',views.enrolled_courses,name='enrolled-courses')
    # path('registered')
]