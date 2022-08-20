from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('Employee',views.Employeedata,name='EMP'),
    path('Department',views.Departmentdata,name='DEP'),
    path('add-new-faculty',views.addfac,name='addFaculty'),
    path('form-data',views.display,name='datadisplay'),
    path('add-new-student',views.addStudent,name='addStudent')
     
]