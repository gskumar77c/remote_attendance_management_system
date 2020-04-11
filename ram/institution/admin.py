from django.contrib import admin
from institution.models import public_announcement,period_slot,department,week_days
import datetime
# Register your models here.
admin.site.register(public_announcement)
# admin.site.register(period_slot)
admin.site.register(department)

# from django.contrib import admin
# from myapp.models import Article

def init_slots(modeladmin, request, queryset):
    # def create_slots(request):
        # print('entered create slots')
    period_slot.objects.all().delete()
    for wd in week_days:
        day = wd[1]
        st_time = '8:00'
        ed_time = '18:00'
        slot_time  =  50
        slot_gap = 10

        time = datetime.datetime.strptime(st_time,'%H:%M')
        end = datetime.datetime.strptime(ed_time,'%H:%M')
        count = 1
        while time <= end :
            fn = time + datetime.timedelta(minutes = slot_time)
            start_time = datetime.datetime.time(time)
            end_time = datetime.datetime.time(fn)
            slot_verbose = day + " slot " + str(count)
            try:
                q = period_slot.objects.filter(slot_verbose=slot_verbose)
                if q.__len__() == 0:
                    slt = period_slot(start_time=start_time,end_time=end_time,day=day,slot_verbose=slot_verbose)
                    slt.save()
                else:
                    print('slot already exists')
            except Exception as e:
                print('error in creating slots')
                raise e
            time += datetime.timedelta(minutes=slot_time + slot_gap)
            count += 1
    # return redirect(reverse("institution.home"))
init_slots.short_description = "create slots"

class period_slotAdmin(admin.ModelAdmin):

    actions = [init_slots]

admin.site.register(period_slot, period_slotAdmin)
