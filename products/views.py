from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from products.models import Product, ProductCategory, Product, Basket
from users.models import User
from django.contrib.auth.decorators import login_required #запрещает доступ к отдельным элементам без авторизации
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse
from users.forms import UserCreationForm
from django.contrib import auth
# Create your views here.

def index(request):
    us = User.objects.filter(username=request.user)
    
    return render(request, 'products/index.html', {'us': us})


def products(request, category_id=None, page_number=1): #категория изначально до клика не передаётся
    
    searchq = request.GET.get('search', '') #поиск по странице
    if searchq:
            posts = Product.objects.filter(Q(name__iregex =searchq) | Q(description__iregex=searchq))
    else:
            posts = Product.objects.all()
    if category_id:        
        posts = Product.objects.filter(category_id=category_id)  #если БД связаны, токакой айдишник у БД, такой и у поста с продуктами
        
    per_page=6 #столько объектов должно быть на странице
    paginator = Paginator(posts, per_page) # функция пагинатор
    products_paginator = paginator.page(page_number) #новая моделька для передачи в темплейт
    context = {
        'title': 'Store-каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all()    
    }
    return render(request, 'products/products.html', context)


def productelement(request,product_id):
        
        return render(request, 'products/productelement.html', {'product': Product.objects.get(id=product_id)} )


@login_required 
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id) #когда выбираешь 
    #продукт получаешь его по айди
    baskets = Basket.objects.filter(user=request.user, product=product)
    #в корзину данного пользователя добавляется ЭТОТ товар
    if not baskets.exists():
        Basket.objects.create(user=request.user,product=product, quantity=1)
        #если не было такого товара то создаём и автоматически сохр
    else:
        basket = baskets.first() #прибавляешь к первому элементу и выводим 
        basket.quantity+=1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER']) #возвращение на ту страницу, где пользователь был

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER']) #возвращение на ту страницу, где пользователь был

def basket_removeall(request, user=None):
    baskets = Basket.objects.filter(user=request.user)
    a = []
    for basket in baskets:
        a.append(basket.user)
        a.append(basket.product)
        a.append(basket.quantity)
        a.append(basket.created_timestamp)
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(str(a) + '\n')
        
    
    return render(request, 'products/orderelement.html')

def basket_removeallfinal(request, user=None):
    baskets = Basket.objects.filter(user=request.user)
    baskets.delete()
    return HttpResponseRedirect(reverse('index'))