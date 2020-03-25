from django.contrib import admin
from institution.models import public_announcements,period_slots,departements
# Register your models here.
admin.site.register(public_announcements)
admin.site.register(period_slots)
admin.site.register(departements)