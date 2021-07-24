from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from .models import OrderItem,Order
from shop.models import Product
import sqlite3



def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})

def order_created(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user=request.user
            order.save()
            
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
        

    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


def place_order(request):
    if request.method=='POST':
        return redirect('/orders/create/place_order')
    return render(request, 'orders/order/created.html')


def order_detail(request):
    user=request.user
    q=Order.objects.raw('''SELECT id FROM auth_user WHERE username=%s''',[user])
    query=Order.objects.raw('''SELECT p.name,oi.price,oi.quantity,o.created,o.delivered FROM orders_orderitem oi INNER JOIN orders_order o on oi.order_id=o.id INNER JOIN shop_product p on  oi.product_id=p.id WHERE o.user_id=%d''',[q])

    return render(request, 'orders/order/order_detail.html', {'list':query})

