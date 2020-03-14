from django.db import models
from django.contrib.auth.hashers import check_password
import os
# from django.contrib.auth.models import User

# Create your models here.

def content_file_name(instance, filename):
    # instance.
    filename = "%s.%s" % (instance.email, "jpg")
    return os.path.join('profile_pictures', filename)

class user(models.Model):

    email=models.EmailField("email",null=False,unique=True)
    full_name=models.CharField(max_length=50,null=False)
    dob=models.DateField("dob",null=False)
    doj=models.DateField("doj",null=False)
    image=models.ImageField("image",null=False,upload_to=content_file_name)
    status=models.BooleanField("status",null=False,default=False)
    description=models.TextField("description",null=True)
    password=models.TextField("password",null=False)    
    

    @classmethod
    def verify_user(cls,emailinput,password):
        # hashed_password=make_password(password)
        
        try:
            user=cls.objects.get(email=emailinput)
            user_password=getattr(user,'password')
            result=check_password(password,user_password)
            return result
        except: 
            return False

        
    # pass
    

