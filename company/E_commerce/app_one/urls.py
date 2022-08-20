from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('store',views.store,name='store'),
    path('product',views.product,name='product'),
    path('cart',views.cart,name='cart'),
    path('check',views.check,name='check'),
 
]