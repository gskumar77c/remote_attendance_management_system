from django.db import models
from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from django.db.models import signals
from django.dispatch import receiver

# from courses.models import courses
from institution.models import department



import os
# from django.contrib.auth.models import User

# Create your models here.

qualification_type=[('student','student'),('ta','ta'),('instructor','instructor')]

def content_file_name(instance,filename):
        # instance.
        # print(filename)
        filename = "%s.%s" % (instance.email, "jpg")
        return os.path.join('profile_pictures', filename)


class user(models.Model):

    # changes
    email=models.EmailField(verbose_name="email ID",null=False,unique=True,primary_key=True)
    # changes
    # email=models.EmailField("email",null=False,unique=True)
    full_name=models.CharField(verbose_name="Full name",max_length=50,null=False)
    dob=models.DateField(verbose_name="Date of birth",null=False)
    doj=models.DateField(verbose_name="Date of join",null=False)
    image=models.ImageField(verbose_name="profile image",null=False,upload_to=content_file_name)
    status=models.BooleanField(verbose_name="account status",null=False,default=False)
    description=models.TextField(verbose_name="breif description",null=True)
    qualification=models.CharField(verbose_name="qualification",max_length=10,choices=qualification_type,null=False,default='student')
    password=models.TextField(verbose_name="password",null=False)    
    
    
    

    @classmethod
    def verify_user(cls,emailinput,password):
        # hashed_password=make_password(password)  
        
        try:
            user=cls.objects.get(email=emailinput)
            user_password=getattr(user,'password')
            result=check_password(password,user_password)
            qualification=getattr(user,'qualification')
            return result,qualification
        except Exception as e:
            print(e)
            return False,""

    @classmethod
    def get_userdetails(cls,emaild):
        result=cls.objects.get(email=emaild)
        result=model_to_dict(result)
        filtered = { your_key: result[your_key] for your_key in ['email','full_name','dob','doj','image','description'] }
        # print(filtered)
        return filtered


class student(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    semester=models.IntegerField(verbose_name="Current semester")


class instructor(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE)

class ta(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    department=models.ForeignKey(department,on_delete=models.CASCADE)




# @receiver(signals.post_save, sender=user)
# def add_user(sender,instance,created, **kwargs):
#     # print(instance.model_to_dict())
#     data=instance.model_to_dict()
#     if data["status"]:
#         type=data["qualification"]
#         if type=="student":
#             res=students.objects.get()
        # res=.objects.get(email=instance)


    # pass
    

