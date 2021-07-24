from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','id', 'home_number', 'street', 'area',
                     'postal_code', 'city','district', 'paid',
                    'created', 'updated','delivered']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
