from django.contrib import admin
from django.urls import path, include
from users.views import login, registrate, profile, logout, addorder
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
     path('registrate/', registrate, name='registrate'),
     path('profile/', profile, name='profile'),
     path('logout/', logout, name='logout'),
     path('addorder/', addorder, name='addorder'),
     
    
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)