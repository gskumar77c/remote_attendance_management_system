from django.shortcuts import render
from profiles.constants.constants import constants
# from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import date
from .models import user,student,instructor,ta
from django.forms.models import model_to_dict

def get_modelclass(qtype):
    print(qtype)
    if qtype=="student":
        return student
    elif qtype=="instructor":
        return instructor
    elif qtype=="ta":
        return ta

def get_modelform(qtype):
    if qtype=="student":
        return student_registration
    elif qtype=="instructor":
        return instructor_registration
    elif type=="ta":
        return ta_registration




def configure_base(arg,name="Not logged in "):
    data=constants.home_page_loggedout

    if arg=='register':        
        data["title"]="Registration"
        data["navbar"]=[["Home","../institution"],["Login","./login"]]
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
        data["navbar"]=[["Home","../institution"],["Register","./register"]]
        data["type"]="Register"
        data["type_link"]="./register"
        data["name"]=name
        data["form"]=login_form()
        return data

    if arg=="dashboard-open":
        data["title"]="Dashboard"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]={}
        user_details=user.get_userdetails(name)
        data["user_details"]=user_details
        return data

    if arg=="dashboard-close":
        data["title"]="Dashboard"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]={}
        user_details=user.get_userdetails(name)
        data["user_details"]=user_details
        data["information"]="Your application is  in pending with the admin"

        return data


def register(request):

    nameheader="Not logged in"
    if "username" in request.session:
        nameheader=request.session["username"]
        redirect('./logout')

    if request.method=="GET":
        data=configure_base("register",nameheader)
        return render(request,"register.html",data)

    else:
        print(request.POST,"<<<"*10)
        qtypeform=request.POST["qtypeform"]
        extended_form_type=get_modelform(qtypeform)

        extended_form=extended_form_type(request.POST,prefix=qtypeform)
        form_user = register_form(request.POST,request.FILES,prefix="user")
        
        if form_user.is_valid() and extended_form.is_valid():
            # hashed_password=make_password(form_user.cleaned_data['password'])
            # qtype=form_user.cleaned_data["qualification"]
            user_email=form_user.cleaned_data["email"]
            form_user = form_user.save(commit=False)
            # form_user.password = hashed_password
            form_user.status=False
            form_user.doj=date.today()
            # form.id=form.email
            # qtype=form_user.cleaned_data["qualification"]
            # extended_form_type=get_modelform(qtype)
            # extended_form=extended_form_type(request.POST,prefix=qtype)
            # print(form_user,":"*10)
            
            # extended_form.email=<user: user object ("+user_email+")>
            try:
                # print(form_user,extended_form)
                form_user.save()
                extended_form=extended_form.save(commit=False)
                # extended_form.save()
                # if extended_form.is_valid():
                #     extended_form.save(commit=False)
                obj=user.objects.get(email=user_email)
                extended_form.user=obj
                extended_form.save()
                #     extended_form.cleaned_data['email']="<user: user object ("+user_email+")>"
                #     print(extended_form,user_email)
                #     extended_form.save()
                
                # else:
                #     print(extended_form.errors)
                #     print("exetended invalid")
                
                

                messages.success(request, f"Registration Successfull")
            except Exception as e:
                print(e)
                messages.success(request,f"Registration Failed")
                return redirect('./register')


            return redirect('./login')
        else:
            print("form not valid\n",form_user.errors,"\n",extended_form.errors,"\n")
            print("not valid")
            messages.success(request, f"Registration Failed")
            return redirect('./register')

# def student_register(request):


def login(request):

    nameheader="Not logged in"
    if "username" in request.session:
        return redirect('./logout')

    if request.method == "GET":
        data=configure_base("login")
        request.session.set_test_cookie()
        return render(request,"login.html",data)
    else:
        if not  request.session.test_cookie_worked():
            messages.success(request,f"cookies not available")
            return redirect('./login')
        form=login_form(request.POST)
        if form.is_valid():
            form=form.cleaned_data
            email=form["email"]
            password=form["password"]
            print(email,password)
            
            result,qualifcation=user.verify_user(email,password)
            if result:
                request.session["username"]=email
                request.session["qualification"]=qualifcation                
                return redirect('./dashboard')
        return redirect('./login')

def dashboard(request):

    nameheader="Not logged in"
    if "username" not in request.session:
        return redirect('./login')
        
    nameheader=request.session["username"]
    user_info=user.objects.get(email=nameheader)
    # user_info=model_to_dict(user_info)
    status=user_info.getattr("status"]
    qtype=user_info["qualification"]
    if not status:
        data=configure_base("dashboard-close",nameheader)
        qualification_based_model=get_modelclass(qtype)
        user_info=qualification_based_model.objects.get(user=nameheader)
        if user_info is None:
            new_form=get_modelform(qtype)
            data["form"]=new_form
        else:
            data

        
    else:
        data=configure_base("dashboard-open",nameheader)        
    
    return render(request,'dashboard.html',data)

def logout(request):
    
    try:
        del request.session['username']
        del request.session["qualification"]
    except KeyError:
        pass
    return redirect('../institution')