from profiles.constants.constants import constants
# from .forms import register_form,student_registration,ta_registration,instructor_registration,login_form
# from .models import user as user_model

def configure_base(arg,name="Not logged in ",additional_dictionary={}):# use additional dictionary for more arguments
    data=constants.home_page_loggedout

    if arg=="attendance":
        data["title"]="Attendance"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]=additional_dictionary["form"]
        
        return data

    
        return data
