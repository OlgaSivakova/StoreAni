from django.contrib import admin
from products.models import Product, ProductCategory, Basket

# Register your models here.

admin.site.register(ProductCategory)


admin.site.register(Product)
admin.site.register(Basket)
#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
#    list_display = ['name', 'price', 'quantity', 'category']
#    fields = ['name', 'description', 'price', 'quantity', 'image', 'image2', 'image3', 'stripe_product_price_id', 'category']
#    search_fields =['name'] 
#    
#
#class BasketAdmin(admin.TabularInline):
#    model = Basket
#    fields = ['product', 'quantity', 'created_timestamp']
#    readonly_fields = ['created_timestamp'] #поле с датой создания заказа должно быть доступно только для чтения

