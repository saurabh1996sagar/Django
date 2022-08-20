from django.shortcuts import redirect, render
from .models import Faculty ,Student
# Create your views here.

def homepage(request):
    student = Student.objects.all()
    return render(request,"index.html" , {'all_student' : student })


def facdata(request):
    faculties = Faculty.objects.all()
    return render(request,'faculty.html',{'all_faculty':faculties }) 

def Saurabhdata(request):
    fac = Faculty.objects.get(faculty_name = 'saurabh')
    # GET METHOD :- get method is for stickly for 1 value ( if salary are same for both faculty the get method show the error , so that's why we use  fillter method )
    # FILLTER METHOD :- Faculty.objects.fillter(salary = 100000.0)  (if the value is not in table the fillter method show the empty page ) ,(in html page we use loop )
    return render(request ,'sau.html',{'faculty' : fac})

def update(request ,pk):
    if request.method == 'POST':
        new_name = request.POST['name']
        new_qualification = request.POST['qualification']
        new_salary = request.POST['salary']

        old_fac =Faculty.objects.get(id=pk)
        old_fac.faculty_name = new_name
        old_fac.qualification = new_qualification
        old_fac.salary = new_salary

        old_fac.save()
        return redirect('faculty')
    else:
      fac = Faculty.objects.get(id = pk)
      return render(request,'update.html',{'faculty':fac})
    # posts =[1,2,3,4,5,6,7]
    # return render (request , 'update.html',{'posts':posts})

def delete(request,pk):
    fac= Faculty.objects.get(id=pk)
    fac.delete()
    return redirect ('faculty')

def post (request, pk ):
    return render(request,'post.html',{'post_number' : pk})

def addFac(request): 
     if request.method == 'POST':
        name = request.POST['name']
        qual = request.POST['qualification']
        sal =request.POST['salary']

        fac = Faculty( faculty_name = name , qualification = qual , salary = sal )  
        fac.save()

        return redirect('faculty')
     return render (request,'add-faculty-form.html')

def addStudent(request):
    if request.method == 'POST':
       entered_name = request.POST['name']
       entered_age = request.POST['age']
       entered_address = request.POST['address']

       s = Student(student_name = entered_name ,age = entered_age ,address =entered_address)
       s.save()

       return redirect('homepage')
    return render (request,'add-student.html')

def display(request):
     if request.method == 'POST':
        fac_name = request.POST['name']
        fac_qualification = request.POST['qualification']
        fac_salary =request.POST['salary']
        print(fac_name, fac_qualification, fac_salary)

        context ={
            'name' : fac_name,
            'qualification' : fac_qualification,
            'salary' : fac_salary
        }
        return render(request,'display.html',context)
     else: 
        return render(request,'display.html')



   











