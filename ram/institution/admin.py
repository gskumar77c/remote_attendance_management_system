from django.contrib import admin
from institution.models import public_announcements,time_table,departements
# Register your models here.
admin.site.register(public_announcements)
admin.site.register(time_table)
admin.site.register(departements)