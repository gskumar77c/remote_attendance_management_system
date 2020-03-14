from django.shortcuts import render
from institution.models import public_announcements
from profiles.constants.constants import constants

# Create your views here.

def configure_base(arg,name):
    data=constants.home_page_loggedout
    if arg=='home':        
        data["title"]="Home"
        if name!="Not logged in":
            data["navbar"]=[["Dashboard","../profiles/dashboard"],["Logout","../profiles/logout"],["Courses","../courses"]]
            data["type"]="Logout"
            data["type_link"]="../profiles/logout"
            data["name"]=name
            data["form"]={}
        else:
            
            data["navbar"]=[["Login","../profiles/login"]]
            data["type"]="Login"
            data["type_link"]="../profiles/login"
            data["name"]=name
            data["form"]={}
        
        return data

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
    res=public_announcements.objects.all()
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