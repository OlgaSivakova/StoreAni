from django.db import models
from users.models import User

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)#unnesesary
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    
    
    def __str__(self):
        return self.name 
    
class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)#float
    quantity = models.PositiveIntegerField(default=0)#always positive int
    image = models.ImageField(upload_to='products_imag', null=True, blank=True)
    image2 = models.ImageField(upload_to='products_imag', null=True, blank=True)
    image3 = models.ImageField(upload_to='products_imag', null=True, blank=True)
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE) #нельзя удалить каегорию из модели категорий, пока все объёекты продуктов не удаляться


    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    
    
class BasketQerrySet(models.QuerySet): #обращение ко всем объектам в словаре квэрри если надо в темплейте вывести всё вне цикла
    def total_sum(self):
        
        return sum(basket.sum() for basket in self)#сумирует 
    #сумму вссех товаров
    
    def total_quantity(self):
        
        return sum(basket.quantity for basket in self)
    
 
    
class Basket(models.Model):
    user=models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    objects =  BasketQerrySet.as_manager()
    
    
    
    def sum(self):
        return self.product.price*self.quantity # к методу потом можно обращаться в шаблоне, он будет считать все показатели для товаров, которые попадают в модельку

    

    
   
    