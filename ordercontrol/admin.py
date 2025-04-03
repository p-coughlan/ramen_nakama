from django.contrib import admin
from .models import OrderWindow

# Register your models here.
class OrderWindowAdmin(admin.ModelAdmin):
    list_display = ['is_open', 'next_delivery_date']

# Register the model with the admin site
admin.site.register(OrderWindow, OrderWindowAdmin)