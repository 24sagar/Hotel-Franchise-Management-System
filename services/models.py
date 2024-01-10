from django.db import models
class Services(models.Model):
    services_icon = models.CharField(max_length=50)
    services_title = models.CharField(max_length=50)
    services_des = models.TextField()

# Create your models here.
