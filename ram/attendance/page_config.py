from profiles.constants.constants import constants
# from .forms import register_form,student_registration,ta_registration,instructor_registration,login_form
# from .models import user as user_model

def configure_base(arg,name="Not logged in ",additional_dictionary={}):# use additional dictionary for more arguments
    data=constants.home_page_loggedout
    data["navbar"]=[["Home","/../institution"],["Logout","/../profiles/logout"],["Courses","/../courses"],["Attendance","../attendance"]]

    if arg=="new attendance":
        data["title"]="New Attendance"
        # data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"],["Attendance","../attendance"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]=additional_dictionary["form"]
        
        return data
    
    if arg=="history_courses":
        data["title"]="Attendance History"
        # data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"],["Attendance","../attendance"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["courses"]=additional_dictionary["courses"]
        
        return data

    if arg=="history_list":
        data["title"]="Attendance History"
        # data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"],["Attendance","../attendance"]]
        data["navbar"]=[["Home","/../institution"],["Logout","/../profiles/logout"],["Courses","/../courses"],["Attendance","/../attendance"]]

        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["entries"]=additional_dictionary["entries"]
        
        return data

    if arg=="details":
        data["title"]="Attendance details"
        # data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"],["Attendance","../attendance"]]
        data["navbar"]=[["Home","/../institution"],["Logout","/../profiles/logout"],["Courses","/../courses"],["Attendance","/../attendance"]]        
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["detail"]=additional_dictionary["details"]
    
        return data


    if arg=="modify":
        data["title"]="Modify Attendance"
        # data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"],["Attendance","../attendance"]]
        data["navbar"]=[["Home","/../institution"],["Logout","/../profiles/logout"],["Courses","/../courses"],["Attendance","/../attendance"]]        
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["student_list"]=additional_dictionary["details"]
        data['id'] = additional_dictionary['id']
    
        return data