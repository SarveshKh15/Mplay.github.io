from django.db import models
from django.contrib.auth.models import User


class Watchlater(models.Model):
    watch_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    video_id=models.CharField(max_length=1000000,default="")
    
    
        