"""ram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from . import views
from vidmi_interface.views import check_pending

urlpatterns = [
    path('', lambda request: redirect('institution/', permanent=False)),
    path('troubleshoot/add',views.initialize_database),
    # path('troubleshoot/delete')
    path('admin/', admin.site.urls),
    path('institution/',include('institution.urls')),
    path('profiles/',include('profiles.urls')),
    path('courses/',include('courses.urls')),
    path('attendance/',include('attendance.urls')),
    path('restapi/',include('restapi.urls'))
]

# the following periodically checks for pending entries
# check_pending(repeat=1*60,repeat_until=None)