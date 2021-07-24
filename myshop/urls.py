from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth  import views as auth_views
from users import views as user_views
from shop import views as shop_views
from orders import views as order_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('front/', shop_views.show, name='front'),
    path('home/', shop_views.prod, name='home'),
    path('order/', order_view.order_create, name='order_create'),
    path('search/', shop_views.search, name='search'),
    path('searched/', shop_views.searched, name='searched'),

    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'AMAZKART'
admin.site.site_title = 'AMAZKART'