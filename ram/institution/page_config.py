from profiles.constants.constants import constants

def configure_base(arg,name="not logged in",additional_dictionary={}):
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
