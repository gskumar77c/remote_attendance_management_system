from django.shortcuts import render
from institution.models import public_announcement as public_announcement_model
from profiles.constants.constants import constants
from .page_config import configure_base

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
    return render(request,'calendar.html',data)