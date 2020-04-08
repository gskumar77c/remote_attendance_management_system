from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from myapi.core import views

urlpatterns = [
    path('teacher_profile/', views.TeacherView.as_view(), name='teacher_profile'),
    path('class_history/', views.ClassHistory.as_view(), name='class_history'),
    path('student_wise /', views.StudentHistory.as_view(), name='student_wise'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]
