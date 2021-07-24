from django.urls import path
from . import views
from django.conf.urls import include, url
import shop.views
app_name = 'shop'
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.front, name='front'),
    path('hom/', views.product_list, name='product_list'),
    path('<slug:category_slug>/see', views.product_front,  name='product_front'),

    path('<slug:category_slug>/', views.product_list,  name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('search/', views.search, name='search'),

    #url(r'^$', views.product_list, name='product_list'),

    
]