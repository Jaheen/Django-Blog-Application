from django.contrib import admin
from  . import models
# Register your models here.
admin.site.register(models.Blog)    #Registers the Database Table with admin site else our database will not be displayed on admin site