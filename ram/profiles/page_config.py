from profiles.constants.constants import constants
from .forms import register_form,student_registration,ta_registration,instructor_registration,login_form
from .models import user as user_model

def configure_base(arg,name="Not logged in ",additional_dictionary={}):# use additional dictionary for more arguments
    data=constants.home_page_loggedout

    if arg=='register':        
        data["title"]="Registration"
        data["navbar"]=[["Home","../institution"],["Login","./login"],["Attendance","./attendance"]]
        data["type"]="Login"
        data["type_link"]="./login"
        data["form_user"]=register_form()
        data["form_student"]=student_registration()
        data["form_instructor"]=instructor_registration()
        data["form_ta"]=ta_registration()
        data["name"]=name
        return data

    if arg=="login":
        data["title"]="Login"
        data["navbar"]=[["Home","../institution"],["Register","./register"],["Attendance","./attendance"]]
        data["type"]="Register"
        data["type_link"]="./register"
        data["name"]=name
        data["form"]=login_form()
        return data

    if arg=="dashboard-open":
        data["title"]="Dashboard"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"],["Attendance","./attendance"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]={}
        user_details=user_model.get_userdetails(name)
        data["user_details"]= user_details
        return data

    if arg=="dashboard-close":
        data["title"]="Dashboard"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Attendance","./attendance"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]={}
        user_details=user_model.get_userdetails(name)
        data["user_details"]=user_details
        data["information"]="Your application is  in pending state with the admin"

        return data
