from django.contrib import admin

from . import models 

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('Name',)}
    list_display=['Name','slug']

admin.site.register(models.CarModel, CarAdmin)
admin.site.register(models.CommentsModel)