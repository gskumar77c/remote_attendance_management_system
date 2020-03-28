from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.all_courses),
    path('coursedetails',views.coursedetails,name= 'course-details'),
    path('floated_courses',views.show_floated_courses,name='floated-courses'),
    path('add_request',views.send_request,name='add-request'),
    path('enrolled_courses',views.enrolled_courses,name='enrolled-courses')
    # path('registered')
]