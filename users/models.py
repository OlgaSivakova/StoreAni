from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    
class Order(models.Model):
    nameord = models.CharField(max_length=256, unique=False)
    email = models.CharField(max_length=256)
    descriptionord = models.TextField(null=True, blank=True)
    adress = models.CharField(max_length=1000)
    contact = models.CharField(max_length=13, default='+')
    
    def __str__(self):
        return f'Заказчик: {self.nameord}'