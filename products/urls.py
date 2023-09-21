from django.contrib import admin
from django.urls import path
from products.views import products, basket_add, basket_remove, productelement, basket_removeall, basket_removeallfinal
app_name = 'products'

urlpatterns = [
    path('products/', products, name='indexp'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('<int:product_id>/',productelement, name='element'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('basketsall/removeall/',basket_removeall, name='basket_removeall'),
    path('basketsallfinal/removeallfinal/',basket_removeallfinal, name='basket_removeallfinal'),
    path('order/orderelement/',basket_removeall, name='orderelement'),
    
]

 