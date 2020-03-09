from django.shortcuts import render
from institution.models import public_announcements

# Create your views here.
def home(request):
    res=public_announcements.objects.all()
    info=[]
    for event in res:
        a=[]
        a.append(event.date)
        a.append(event.info)
        info.append(a)
    

    return render(request,'calendar.html',{"title":"wel","info":info})