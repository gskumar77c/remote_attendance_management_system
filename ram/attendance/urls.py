from django.urls import path,include
from . import views

urlpatterns=[
    path('new', views.web_input),
    path('history', views.history),
    path('details/<int:pk>',views.details),
    path('modify/<int:pk>',views.modify)
    # path('coursedetails',views.coursedetails,name= 'course-details'),
    # path('floated_courses',views.show_floated_courses,name='floated-courses'),
    # path('add_request',views.send_request,name='add-request'),
    # path('enrolled_courses',views.enrolled_courses,name='enrolled-courses')
    # path('registered')
]