from django.shortcuts import render
from profiles.constants.constants import constants
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import date


def configure_base(arg,name="none"):
    data=constants.home_page_loggedout
    if arg=='register':        
        data["title"]="Registration"
        data["navbar"]=[["Home","../institution"],["Login","./login"]]
        data["type"]="Login"
        data["type_link"]="./login"
        data["form"]=register_form()
        return data
    if arg=="login":
        data["title"]="Login"
        data["navbar"]=[["Home","../institution"],["Register","./register"]]
        data["type"]="Register"
        data["type_link"]="./register"
        data["form"]=login_form()
        return data
    if arg=="dashboard":
        data["title"]="Dashboard"
        data["navbar"]=[["Home","../institution"],["Logout","./logout"],["Courses","../courses"]]
        data["type"]="Logout"
        data["type_link"]="./logout"
        data["name"]=name
        return data


def register(request):

    if request.method=="GET":
        data=configure_base("register")
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
            return redirect('../login')
        else:
            messages.success(request, f"Registration Failed")
            return redirect('./register')


def login(request):
    if request.method == "GET":
        data=configure_base("login")
        request.session.set_test_cookie()
        return render(request,"login.html",data)
    else:
        if not  request.session.test_cookie_worked():
            messages.success(request,f"cookies not available")
            return redirect('./login')
        form=login_form(request.POST)
        email=form.cleaned_data["email"]
        password=form.cleaned_data["password"]    
        result=user.verify_user(email,password)
        if result:
            request.session["username"]=email
            return redirect('./dashboard')
def dashboard(request):
    username=request.session["username"]
    if username is  None:
        return redirect('./login')
    data=configure_base("dashboard")
    return render(request,'dashboard.html',data)

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('../institution')