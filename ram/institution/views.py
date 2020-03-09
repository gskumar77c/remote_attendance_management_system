from django.shortcuts import render
from institution.models import public_announcements

# Create your views here.
def announcement_reader(arg):
    info=[]
    for event in arg:
        a=[]
        a.append(event.date)
        a.append(event.info)
        info.append(a)
    return info

def home(request):
    res=public_announcements.objects.all()
    info=announcement_reader(res)
    title="Home"
    navbar=[["login","#"]]
    # handle logged in state differently

    return render(request,'calendar.html',{"title":"wel","info":info,'navbar':navbar})