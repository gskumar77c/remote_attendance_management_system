from django.db import models

# Create your models here.
class public_announcements(models.Model):
    date=models.DateTimeField('date')
    info=models.TextField('info')