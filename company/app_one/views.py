from sys import stdout
from django.shortcuts import render, redirect 
from .models import Employee,Department , Student
# from .models import Department , Student

# Create your views here.
def home(request):
    student = Student.objects.all()
    return render(request,'index.html',{'all_student' : student})

def Employeedata(request):
    Emp = Employee.objects.all()
    return render(request,'Emp.html',{'all_Employee':Emp})   

def Departmentdata(request):
    Dep = Department.objects.all()
    return render(request,'Dep.html',{"all_Department":Dep})

def update(request,pk):
    if  request.method == 'POST':
        new_name = request.POST['name']   
        new_qualification = request.POST['qualification'] 
        new_salary = request.POST['salary']

    
def addStudent(request):
    if request.method == 'POST' :
        d_name = request.POST['name']   
        d_age = request.POST['age']    
        d_address = request.POST['address']    

        d = Student( Student_name=d_name, age=d_age, address=d_address)
        d.save()

        return redirect("home")

    return render(request,'add-student.html')  

def addfac(request):
    if request.method == 'POST':
        name = request.POST['name']
        qual = request.POST['qualification']
        sal = request.POST['salary']

        context = {
           'name' : name,
           'qualification' : qual,
           'salary' : sal,
        }
        return render(request,'add-faculty-form.html',context)
    else :
        return render(request,'add-faculty-form.html')    

def display(request):
    if request.method == 'POST':
        fac_name = request.POST['name']
        fac_qualification = request.POST['qualification']
        fac_salary = request.POST['salary']
        print(fac_name, fac_qualification , fac_salary )

        context = {
           'name' : fac_name,
           'qualification' : fac_qualification,
           'salary' : fac_salary,
        }

        return render(request,"display.html",context)
    else:
        return render(request,'display.html',)    