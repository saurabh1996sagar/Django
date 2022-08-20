from django.shortcuts import redirect, render

from app_one.models import Employee


# Create your views here.
def index(request):
    emp = Employee.objects.all()
    return render(request,'index.html',{'all_emp' : emp})



def update(request):
    return render(request,'update.html')



def delete(request,pk):
    emp = Employee.objects.get(id = pk)
    emp.delete()
    return redirect('index')




