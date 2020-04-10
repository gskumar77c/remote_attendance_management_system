from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.all_courses,name='courses.all'),
    path('coursedetails',views.coursedetails,name= 'courses.details'),
    path('floated_courses',views.show_floated_courses,name='courses.floated'),
    path('enrolled_courses',views.enrolled_courses,name='courses.enrolled'),
    path('joined_courses',views.joined_courses,name='courses.joined'),
    path('student_requests',views.student_requests,name='courses.requests')
    # path('registered')
]