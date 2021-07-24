from django.urls import path
from . import views
from django.conf.urls import include, url

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    #url(r'^create$', views.order_create, name='order_create'),
    #path('<slug:category_slug>/', views.order_create, name='order_create'),
    path('create/place_order/', views.place_order, name='place_order'),
   #path('place_order/', views.place_order, name='place_order'),
    #url(r'^place_order$', views.place_order, name='place_order'),
    path('create/order_created/', views.order_created, name='order_created'),
    path('order/', views.order_detail, name='order_detail'),

]
