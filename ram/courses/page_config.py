from profiles.constants.constants import constants
from profiles.models import user
from django.urls import reverse

def configure_base(arg,name,additional_dictionary={}):
    data=constants.home_page_loggedout
    usr = user.objects.get(email=name)

    # common to all
    # if usr.status == False:
    #     data["navbar"]=[["Dashboard",reverse("insti.logout")],["All Courses","../courses"],["Logout","../profiles/logout"]]
    
    if additional_dictionary['qtype'] == 'student':
        data["navbar"]=[["Home",reverse('institution.home')],["Logout",reverse("profiles.logout")],["All Courses",reverse("courses.all")],["Enrolled Courses",reverse("courses.enrolled")],["Add Courses",reverse("courses.floated")],["Attendance",reverse("attendance.home")]]

        # data["navbar"]=[["Dashboard","../profiles/dashboard"],["All Courses","../courses"],["Enrolled Courses","../courses/enrolled_courses"],["Add Courses","../courses/floated_courses"],["Logout","../profiles/logout"],["Attendance","../attendance"]]
    else:
        data["navbar"]=[["Home",reverse('institution.home')],["Logout",reverse("profiles.logout")],["All Courses",reverse("courses.all")],["Joined Courses",reverse("courses.joined")],["Add Courses",reverse("courses.floated")],["Attendance",reverse("attendance.home")]]
        # data["navbar"]=[["Dashboard","../profiles/dashboard"],["All Courses","../courses"],["Joined Courses","../courses/joined_courses"],["Float Courses","../courses/floated_courses"],["Logout","../profiles/logout"],["Attendance","../attendance"]]
    data["type"]="Logout"
    data["type_link"]=reverse("profiles.logout")
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