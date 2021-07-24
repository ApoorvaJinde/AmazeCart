from django.db import models
from shop.models import Product
import datetime
from datetime import timedelta,datetime
from users.models import User
class Order(models.Model):
    user = models.ForeignKey(User,
                                 related_name='user',
                                 on_delete=models.CASCADE,null=True)
    street   =models.CharField(max_length=250,null=True)
    area =models.CharField(max_length=250,null=True)
    district =models.CharField(max_length=250,null=True) 
    home_number = models.CharField(max_length=250,null=True)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    delivered = models.DateTimeField(default=datetime.now().date()+timedelta(days=15))
   

    class Meta:
        ordering = ('-created','delivered')

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

   
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
