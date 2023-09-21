from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from products.models import Product, ProductCategory, Product, Basket, OrderProduct
from users.models import User
from django.contrib.auth.decorators import login_required #запрещает доступ к отдельным элементам без авторизации
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request, category_id=None, page_number=1): #категория изначально до клика не передаётся
    
    searchq = request.GET.get('search', '')
    if searchq:
            posts = Product.objects.filter(Q(name__iregex =searchq) | Q(description__iregex=searchq))
    else:
            posts = Product.objects.all()
    if category_id:        
        posts = Product.objects.filter(category_id=category_id) 
        
    per_page=3
    paginator = Paginator(posts, per_page)
    products_paginator = paginator.page(page_number)
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
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if not baskets.exists():
        Basket.objects.create(user=request.user,product=product, quantity=1)
    else:
        basket = baskets.first()
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
        a.append(basket.product)
        a.append(basket.quantity)
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(str(a))
    
    return render(request, 'products/orderelement.html')

def basket_removeallfinal(request, user=None):
    baskets = Basket.objects.filter(user=request.user)
    baskets.delete()
    return HttpResponseRedirect(reverse('index'))