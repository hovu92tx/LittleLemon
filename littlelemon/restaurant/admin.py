from django.contrib import admin
from .models import Rating, Menu, Booking, Order, Category, Cart

admin.site.register(Booking)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(Cart)