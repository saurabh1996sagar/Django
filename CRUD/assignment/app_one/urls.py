from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
      path('admin/', admin.site.urls),
      path('',views.index,name='index'),
      path('update',views.update,name='update'),
      path('delete/<str : pk>',views.delete,name='delete')
]