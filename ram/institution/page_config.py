from profiles.constants.constants import constants
from django.urls import reverse

def configure_base(arg,name="not logged in",additional_dictionary={}):
    data=constants.home_page_loggedout
    if arg=='home':        
        data["title"]="Home"
        if name!="Not logged in":
            data["navbar"]=[["Dashboard","../profiles/dashboard"],["Logout","../profiles/logout"],["Courses","../courses"],["Attendance","../attendance"]]
            data["navbar"]=[["Home",reverse('institution.home')],["Logout",reverse("profiles.logout")],["Courses",reverse("courses.all")],["Attendance",reverse("attendance.home")]]
            data["type"]="Logout"
            data["type_link"]=reverse("profiles.logout")
            data["name"]=name
            data["form"]={}
        else:
            
            data["navbar"]=[["Login","../profiles/login"],["Register",reverse("profiles.register")]]
            data["type"]="Login"
            data["type_link"]=reverse("profiles.login")
            data["name"]=name
            data["form"]={}
        
        return data
