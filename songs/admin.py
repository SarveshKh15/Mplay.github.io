from django.contrib import admin

# Register your models here.
from .models import Music
from .models.category import Category
from .models.watchlater import Watchlater
from .models.channel import Channel
admin.site.register(Music)
admin.site.register(Category)
admin.site.register(Watchlater)

admin.site.register(Channel)