from django.contrib import admin
from store.models import Laptop, Cart, CartItem, Order
# Register your models here.
admin.site.register(Laptop)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
