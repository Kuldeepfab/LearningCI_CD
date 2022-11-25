from multiprocessing import context
import re
from django.shortcuts import render, HttpResponse
from datetime import datetime
from homeApp.models import Contact

# Create your views here.

def index(request):
    context = {
        "var1":"My self Peedluek",
        "var2":"I am from INDIA"
    }
    return render(request,'index.html',context) # return the index.html page , which is stored in template folder , also have context(variable)
    #return HttpResponse("This is HomePage created by kuldeep")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is AboutPage created by kuldeep")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is ServicesPage created by kuldeep")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contacts.html')
    #return HttpResponse("This is ContactPage created by kuldeep")