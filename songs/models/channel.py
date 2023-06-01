from django.db import models
from django.contrib.auth.models import User
class Channel(models.Model):
    channel_id=models.AutoField(primary_key=True)
     
    name=models.CharField(max_length=1000,default="USER")
     
    music=models.CharField(max_length=1000000)
    
    def __str__(self):
        return self.name