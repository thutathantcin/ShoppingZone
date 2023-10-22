from django.db import models

# Create your models here.
class Cities(models.Model):
    cityName =models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(max_length=10, blank=True, null=True)
    createdUser =models.CharField(max_length=255, blank=True, null= True)
    updatedUser =models.CharField(max_length=255, blank=True, null=True)
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now_add=True)
