from django.shortcuts import render
from profiles.constants.constants import constants
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import date


def configure_base(arg,name="Not logged in "):
    data=constants.home_page_loggedout

    if arg=='register':        
        data["title"]="Registration"
        data["navbar"]=[["Home","../institution"],["Login","./login"]]
        data["type"]="Login"
        data["type_link"]="./login"
        data["form"]=register_form()
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
    if arg=="dashboard":
        data["title"]="Dashboard"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        data["form"]={}
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
        form = register_form(request.POST,request.FILES)
        if form.is_valid():
            hashed_password=make_password(form.cleaned_data['password'])
            form = form.save(commit=False)
            form.password = hashed_password
            form.status=False
            form.doj=date.today()
            form.save()
            messages.success(request, f"Registration Successfull")
            return redirect('./login')
        else:
            messages.success(request, f"Registration Failed")
            return redirect('./register')


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
            # print(type(form),form,"<<<<<<<<<")    
            result=user.verify_user(email,password)
            if result:
                request.session["username"]=email
                return redirect('./dashboard')
        return redirect('./login')

def dashboard(request):

    nameheader="Not logged in"
    if "username" in request.session:
        nameheader=request.session["username"]
    else:
        return redirect('./login')
    data=configure_base("dashboard",nameheader)
    return render(request,'dashboard.html',data)

def logout(request):
    
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('../institution')