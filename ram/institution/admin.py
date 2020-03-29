from django.contrib import admin
from institution.models import public_announcement,period_slot,department
# Register your models here.
admin.site.register(public_announcement)
admin.site.register(period_slot)
admin.site.register(department)