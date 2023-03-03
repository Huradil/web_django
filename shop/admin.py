from django.contrib import admin
from .models import Purchase,Item

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name','age','item']
    search_fields = ['name','item']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ['name','price']

