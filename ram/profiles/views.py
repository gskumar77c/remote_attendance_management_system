from django.shortcuts import render
from profiles.constants.constants import constants
# from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from datetime import date
from .models import user as user_model
from .models import student as student_model
from .models import instructor as instructor_model
from .models import ta as ta_model
from .page_config import configure_base

# from .models import user,student,instructor,ta as user_model,student_model,instructor_model,ta_model
from django.forms.models import model_to_dict

def get_modelclass(qtype):
    # print(qtype)
    if qtype=="student":
        return student_model
    elif qtype=="instructor":
        return instructor_model
    elif qtype=="ta":
        return ta_model

def get_modelform(qtype):
    if qtype=="student":
        return student_registration
    elif qtype=="instructor":
        return instructor_registration
    elif qtype=="ta":
        return ta_registration






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
            
            user_email=form_user.cleaned_data["email"]
            form_user = form_user.save(commit=False)
            form_user.status=False
            form_user.doj=date.today()
            try:
                form_user.save()
                extended_form=extended_form.save(commit=False)
                obj=user_model.objects.get(email=user_email)
                extended_form.user=obj
                extended_form.save()
                messages.success(request, f"Registration Successfull")
            except Exception as e:
                print(e)
                messages.success(request,f"Registration Failed")
                return redirect('./register')


            return redirect('./login')
        else:
            print("form not valid\n",form_user.errors,"\n",extended_form.errors,"\n")
            # print("not valid")
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
            # print(email,password)
            
            result,qualifcation=user_model.verify_user(email,password)
            if result:
                request.session["username"]=email
                request.session["qualification"]=qualifcation                
                return redirect('./dashboard')
        messages.success(request, f"Credentials wrong")
        return redirect('./login')

def dashboard(request):

    nameheader="Not logged in"
    if "username" not in request.session:
        return redirect('./login')
        
    nameheader=request.session["username"]
    user_info=user_model.objects.get(email=nameheader)
    status=getattr(user_info,"status")
    qtype=getattr(user_info,"qualification")

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