from django.shortcuts import render
from .models import Form

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def facdata(request):
    forms = Form.objects.all()
    return render(request,'form.html',{'all_form': forms})