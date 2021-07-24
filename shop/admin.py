from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated','brand','color','model']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available','brand','color','model']
    prepopulated_fields = {'slug': ('name',)}
