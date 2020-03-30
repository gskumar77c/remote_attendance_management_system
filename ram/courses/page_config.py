from profiles.constants.constants import constants

def configure_base(arg,name="not logged in",additional_dictionary={}):
    data=constants.home_page_loggedout
    if arg=='courses':        
        data["title"]="courses"
        if name == "logged_in":
            data["navbar"]=[["Dashboard","../profiles/dashboard"],["Enrolled Courses","../courses/enrolled_courses"],["Floated Courses","../courses/floated_courses"],["Logout","../profiles/logout"]]
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