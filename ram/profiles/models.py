from django.db import models
from django.contrib.auth.hashers import make_password

# from django.contrib.auth.models import User

# Create your models here.

class user(models.Model):

    email=models.EmailField("email",null=False,unique=True)
    full_name=models.CharField(max_length=50,null=False)
    dob=models.DateField("dob",null=False)
    doj=models.DateField("doj",null=False)
    image=models.ImageField("image",null=False)
    status=models.BooleanField("status",null=False)
    description=models.TextField("description",null=True)
    password=models.TextField("password",null=False)    
    

    @classmethod
    def verify_user(cls,emailinput,password):
        # hashed_password=make_password(password)
        user=cls.object.get(email=emailinput)
        if type(user)==None:
            return False;
        hashed_password=make_password(password)
        if user["password"]==hashed_password:
            return True
        return False
    # pass
    

