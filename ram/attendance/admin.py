from django.contrib import admin
from .models import attendance_register,api_queue
# Register your models here.
admin.site.register(attendance_register)
admin.site.register(api_queue)