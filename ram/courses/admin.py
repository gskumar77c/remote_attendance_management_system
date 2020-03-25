from django.contrib import admin
from courses.models import courses,attendance,course_student_log,course_instructor_log,course_ta_log,time_table
# Register your models here.
admin.site.register(courses)
admin.site.register(attendance)
admin.site.register(course_student_log)
admin.site.register(course_instructor_log)
admin.site.register(course_ta_log)
admin.site.register(time_table)