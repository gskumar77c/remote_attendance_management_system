from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.contrib import messages

# Create your views here.
def all_courses(request):
    if "username" not in request.session:
        return redirect('../profiles/login')
    username=request.session["username"]
    qtype=request.session["qualification"]
    