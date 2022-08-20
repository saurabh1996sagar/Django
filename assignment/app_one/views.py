from django.shortcuts import redirect, render
from .models import  Employee

# Create your views here.
def index(request):
    emp = Employee.objects.all()
    return render (request,'index.html',{'all_emp': emp})


def update(request, pk): 
    if request.method == 'POST':
        new_id = request.POST['id']
        new_name = request.POST['name']
        new_address = request.POST['address']

        old_emp =Employee.objects.get(id=pk)
        old_emp.Employee_id = new_id
        old_emp.Employee_name = new_name
        old_emp.Address = new_address

        old_emp.save()
        return redirect('index')

    else:
      emp = Employee.objects.get(id = pk)
      return render(request,'update.html',{'employee':emp})
    


def delete(request,pk):
    emp_d = Employee.objects.get(id=pk)
    emp_d.delete()
    return redirect('index')
 


def addemp(request):
    if request.method == 'POST':
        emp_id = request.POST['id']
        emp_name = request.POST['name']
        emp_add = request.POST['address']

        emp_data = Employee(Employee_id = emp_id , Employee_name = emp_name , Address = emp_add) 
        emp_data.save()

        return redirect ("emp")

    return render(request,'add.html')
   


