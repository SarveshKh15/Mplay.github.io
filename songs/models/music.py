from django.db import models
from .category import Category 

class Music(models.Model):
    music_id=models.AutoField
    music_name=models.CharField(max_length=50)
    music_singer=models.CharField(max_length=50)
    music_movie=models.CharField(max_length=100)
    music_durations=models.CharField(max_length=15)
    image=models.FileField( upload_to='songs/covers',max_length=None)
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    
    audio=models.FileField(upload_to='songs/audio', max_length=100)
    
    pub_date=models.DateField()
    
    def __str__(self):
        return self.music_name
        
    
    
     
        
    @staticmethod
    def get_all_Music():
        return Music.objects.all()
        
    @staticmethod
    def get_by_id(category_id):
        if category_id:
            return Music.objects.filter(category=category_id)
        else:
            return Music.objects.all()
        
# class Category(models.Model):
#     title=models.CharField(max_length=100)
#     image=models.ImageField(upload_to='songs/cat_imgs')
    
   
        
#     def __str__(self):
#         return self.title
    
