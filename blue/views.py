from django.shortcuts import render,redirect
from .models import Products
#from .forms import Products
from django.http import HttpResponse
from blue.models import Products



# Create your views here.

def login(request):
    return render(request,'login.html')
def layout(request):
    return render(request,'layout.html')
def table(request):
    return render(request,'table.html')
def create(request):
    return render(request,'create.html')

def signup(request):
    if request.method == "POST":
       PortName = request.POST['portname']
       Contact = request.POST['contact']
       Location = request.POST['location']
       Status = request.POST['status']

       new_applicant = Products(PortName=PortName,Contact=Contact,Location=Location,Status=Status)
       new_applicant.save()
    return render(request,'signup.html')

def new_applicants(request):
    appls = Products.objects.all()
    return render(request,'table.html',{'appls':appls})


    



