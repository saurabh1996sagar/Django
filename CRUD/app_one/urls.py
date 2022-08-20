from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name = 'homepage'),
    path('faculty-data',views.facdata ,name='faculty'),
    path('saurabh_data',views.Saurabhdata, name='saurabh_data'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('update/<str:pk>',views.update,name='update'),
    path('add-new-faculty',views.addFac , name='addFaculty'),
    path('form-data',views.display,name='datadisplay'),
    path('add-new-student',views.addStudent,name='addStudent'),
    path('post/<str:pk>',views.post,name='post'),

]