from django.contrib import admin
from users.models import User, Order

# Register your models here.

admin.site.register(Order)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
    