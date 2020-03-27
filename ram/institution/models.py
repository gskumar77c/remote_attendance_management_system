from django.db import models
# from courses.models import courses
import courses
#  as courses_module

week_days=[('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday'),('friday','friday'),('saturday','saturday'),('sunday','sunday'),]
# Create your models here.
class public_announcements(models.Model):
    
    date=models.DateTimeField(name='date')
    info=models.TextField(name='info')

class departements(models.Model):
	name=models.CharField(name="department",max_length=20,unique=True,null=False)

	def __str__(self):
		return self.department

class period_slots(models.Model):
	day=models.CharField(verbose_name="week day",choices=week_days,max_length=10)
	start_time=models.TimeField(verbose_name="slot start time")
	end_time=models.TimeField(verbose_name="slot end time")
	

	# @classmethod
	# def return_slot(cls,time):
	# 	result=cls.objects.get(start_time<=time,end_time=>time)
	# 	return result