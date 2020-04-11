from django.db import models

# Create your models here.


class address(models.Model):
    ipaddr=models.GenericIPAddressField(verbose_name="IP adress")
    port=models.IntegerField(verbose_name="Port Number")
    token=models.CharField(max_length=100,verbose_name="API Token")

    @classmethod
    def connection_info(cls):
        res=address.object.all()[0]
        return res.ipaddr,res.port,res.token


    
