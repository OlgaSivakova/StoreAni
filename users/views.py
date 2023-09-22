from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, OrderForm
from django.contrib import auth, messages
from products.models import Basket
from users.models import Order
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    if request.method =='POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid:
            username = request.POST['username'] #posr запрос это словраь, из которого по ключам вытягиваем значение
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) #так программа понимает, какие права есть у пользователя с такими данными
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else: #если гет, то просто отобразить саму форму
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registrate(request):
    if request.method =='POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    contex = {'form':form}
    return render(request, 'users/register.html', contex)

@login_required 
def profile(request):
    if request.method =='POST':
        form = UserProfileForm(instance=request.user,data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация завершена успешно!') #успешная регистрация сообщение
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:    
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)
    
    context = {'title':"Store-Профиль",
               'form':form,
                'baskets': Basket.objects.filter(user=request.user) #не показывать в корзине чужие товары
              
    }
    
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def addorder(request):
    error = ''
    if request.method == "POST":
       
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.nameord= request.user
            order.email = form.cleaned_data['email']
            order.descriptionord = form.cleaned_data['descriptionord']
            order.adress = form.cleaned_data['adress']
            order.contact= form.cleaned_data['contact']
            order.save()
            return redirect('products:basket_removeall')
        else:
            error = form.errors
           
    else:
        form = OrderForm()

    return render(request, 'users/addorder.html', {'form': form, 'errors':error})
  