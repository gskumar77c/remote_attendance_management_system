from django.shortcuts import render,redirect
from institution.models import public_announcement as public_announcement_model
from profiles.constants.constants import constants
from .page_config import configure_base
from institution.models import period_slot,week_days
import datetime
from django.urls import reverse
# Create your views here.



def announcement_reader(arg):
    info=[]
    # print("yes",arg)
    for event in arg:
        a=[]
        # print(info)
        a.append(event.date)
        a.append(event.info)
        info.append(a)
    return info

def home(request):
    res=public_announcement_model.objects.all()
    info=announcement_reader(res)
    title="Home"
    navbar=[["login","#"]]

    name="Not logged in"
    if "username" in request.session:
        name=request.session["username"]
    
    # handle logged in state differently
    data=configure_base("home",name )
    # print(info)
    data["info"]=info
    # create_slots()
    return render(request,'calendar.html',data)



def create_slots(request):
    # print('entered create slots')
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
    return redirect(reverse("institution.home"))
    # print('exit create slots')

