from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def store(request):
    return render(request,'store.html')

def product(request):
    return render(request,'product.html')    

def cart(request):
    return render(request,'cart.html')

def check(request):
    return render(request,'check.html')



