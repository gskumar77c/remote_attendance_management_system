from django.contrib import admin
from .models import user
from .models import students

admin.site.register(user)
admin.site.register(students)