from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.all_courses),
    path('coursedetails',views.coursedetails,name= 'course-details'),
    path('floated_courses',views.show_floated_courses,name='floated-courses'),
    path('enrolled_courses',views.enrolled_courses,name='enrolled-courses'),
    path('joined_courses',views.joined_courses,name='joined-courses'),
    path('student_requests',views.student_requests,name='student-requests')
    # path('registered')
]