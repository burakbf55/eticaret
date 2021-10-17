from django.contrib import admin
from .models import ShoppingCartItem, ShoppingCart
# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)