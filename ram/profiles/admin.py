from django.contrib import admin
from .models import user
from .models import students,instructor,ta

admin.site.register(user)
admin.site.register(students)
admin.site.register(instructor)
admin.site.register(ta)