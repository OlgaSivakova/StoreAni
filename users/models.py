from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    
class Order(models.Model):
    nameord = models.CharField(max_length=256)
    lastnameord = models.CharField(max_length=256)
    descriptionord = models.CharField(max_length=256)
    adress = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    
    def __str__(self):
        return f'Заказчик: {self.nameord}'