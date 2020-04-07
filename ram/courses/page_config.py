from profiles.constants.constants import constants

def configure_base(arg,name="not logged in",additional_dictionary={}):
    data=constants.home_page_loggedout

    # common to all
    if additional_dictionary['qtype'] == 'student':
        data["navbar"]=[["Dashboard","../profiles/dashboard"],["All Courses","../courses"],["Enrolled Courses","../courses/enrolled_courses"],["Add Courses","../courses/floated_courses"],["Logout","../profiles/logout"]]
    else:
        data["navbar"]=[["Dashboard","../profiles/dashboard"],["All Courses","../courses"],["Joined Courses","../courses/joined_courses"],["Float Courses","../courses/floated_courses"],["Logout","../profiles/logout"]]
    data["type"]="Logout"
    data["type_link"]="../profiles/logout"
    data["name"]=name
    data["form"]={}
    data['qtype'] = additional_dictionary['qtype']


    # specific to each view
    if arg=='courses':
        data["title"]="courses"

    elif arg=='course-details':
        data['title'] = 'course details'

    elif arg == 'floated-courses' :
        if additional_dictionary['qtype'] == 'student':
            data['title'] = 'Add courses'
        else :
            data['title'] = 'Float courses'

    elif arg == 'enrolled-courses':
        data['title'] = 'enrolled courses'

    elif arg == 'joined-courses':
        data['title'] = 'joined courses'

    elif arg == 'student-requests':
            data['courseid'] = additional_dictionary['courseid']
            data['list_type'] = additional_dictionary['list_type']
            if additional_dictionary['list_type'] == 'requests':
                data['title'] = 'Add Requests'
            elif additional_dictionary['list_type'] == 'enrolled':
                data['title'] = 'Enrolled Students'
            else:
                data['title'] = 'Attendance of Enrolled students'
 


    return data