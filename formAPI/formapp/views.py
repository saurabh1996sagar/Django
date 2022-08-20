from django.shortcuts import render
from formapp.forms import LoginForm, SimpleForm, StudentForm

# Create your views here.

def next(request):
    return render (request,'next.html')

def index(request):
 if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        age = form.cleaned_data['age']
        context ={
           'name' : username,
           'pass' : password,
           'aga'  : age
        }
        return render(request,'next.html',context)

 else:
        form = LoginForm()
        return render(request,'index.html',{'login_form': form})  


def widgets(request):
    form  = SimpleForm()
    context = {'form': form}
    return render(request,'form-two.html',context)

def studentForm(request):
    stform = StudentForm()
    return render (request,'student-form.html',{'form': stform})










