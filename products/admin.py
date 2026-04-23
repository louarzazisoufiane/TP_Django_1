from django.contrib import admin
from .models import Product, Category
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created_at', 'description']
    search_fields = ['name', 'description']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']
    search_fields = ['name']
    list_filter = ['name']