from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='songs/cat_imgs')
    
   
   
        
    def __str__(self):
        return self.title
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
# @staticmethod
# def get_by_id(category_id):
#     return Music.objects.filter(category=category_id)
