from django.db import models
from django.contrib import admin
class Car(models.Model):
 car_name = models.CharField() 
 car_model = models.CharField()
 car_colour=models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name','car_model','car_colour')

