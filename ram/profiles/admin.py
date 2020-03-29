from django.contrib import admin
from .models import user
from .models import student,instructor,ta

admin.site.register(user)
admin.site.register(student)
admin.site.register(instructor)
admin.site.register(ta)