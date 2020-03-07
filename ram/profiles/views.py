from django.shortcuts import render
from classes.objects import links

# Create your views here.

        
def home(request):
    
    f7=["login7","/"]
    f6=["login6","/"]
    f5=["login5","/"]
    f4=["login4","/"]
    f3=["login3","/"]
    f2=["login2","#"]
    f1=["login1",""]
    return render(request,'home.html',{'title':'Home','test':'success','navbar':[f1,f1,f1,f1,f1,f2,f3,f4,f5,f6,f7]})