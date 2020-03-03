from django.urls import path,include
from . import views



urlpatterns = [
    path('authinterface/',views.AuthenticationInterface,name = 'auth-interface'),
    path('admin_home/',views.admin_home,name='admin-home'),
    path('faculty_home/',views.faculty_home,name='faculty-home'),
    path('student_home/',views.student_home,name='student-home'),
    path('',include('business_entities.urls')),
    
]
