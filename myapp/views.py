from django.shortcuts import render
from myapp.models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact_us(request):
    if request.method=="POST":
       name= request.POST.get("name")
       em= request.POST.get("email")
       sub = request.POST.get("subject")
       msz= request.POST.get("message")
       obj =Contact(name=name, email=em, subject=sub, message=msz)
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


