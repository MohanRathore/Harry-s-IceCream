from datetime import datetime
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
 
# Create your views here.
def index(request):
    context = {
        'variable':"this is mohan kumar"
    }
    return render(request, "index.html",context)
def about(request):
    context = {
        
    }
    return render(request, "about.html",context)
   
def services(request):
    context = {
        
    }
    return render(request, "services.html",context)
   
def contact(request):
    context = {
        
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your messege has been sent.')
        def __str__(self):
            return self.name
        
    return render(request, "contact.html",context)
   