from django.db import models
from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from django.db.models import signals
from django.dispatch import receiver
from courses.models import courses
from institution.models import departements
import os
# from django.contrib.auth.models import User

# Create your models here.

qualification_type=[('student','student'),('ta','ta'),('instructor','instructor')]



class user(models.Model):

    
    email=models.EmailField("email",null=False,unique=True)
    full_name=models.CharField(max_length=50,null=False)
    dob=models.DateField("dob",null=False)
    doj=models.DateField("doj",null=False)
    image=models.ImageField("image",null=False,upload_to=content_file_name)
    status=models.BooleanField("status",null=False,default=False)
    description=models.TextField("description",null=True)
    qualification=models.CharField("Qualification",max_length=10,choices=qualification_type,null=False,default='student')
    password=models.TextField("password",null=False)    
    
    def content_file_name(self,instance, filename):
        # instance.
        filename = "%s.%s" % (instance.email, "jpg")
        return os.path.join('profile_pictures', filename)

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

    @classmethod
    def get_userdetails(cls,emaild):
        result=cls.objects.get(email=emaild)
        result=model_to_dict(result)
        filtered = { your_key: result[your_key] for your_key in ['email','full_name','dob','doj','image','description'] }
        print(filtered)
        return filtered

@receiver(signals.post_save, sender=user)
def add_user(sender,instance,created, **kwargs):
    # print(instance.model_to_dict())
    data=instance.model_to_dict()
    if data["status"]:
        type=data["qualification"]
        if type=="student":
            res=students.objects.get()
        # res=.objects.get(email=instance)

class students(models.Model):
    id=models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    courses_completed=models.ManyToManyField(courses)

class instructor(models.Model):
    id=models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    department=models.ForeignKey(departements)

class ta(models.Model):
    id=models.OneToOneField(user,on_delete=models.CASCADE,primary_key=True)
    department=models.ForeignKey(departements)






    # pass
    

