from django.shortcuts import render
from django.http import HttpResponse
def res(request):
   context={'home':'active'}
   return render(request,"index.html",context)
def service(request):
   context={'services':'active'}
   return render(request,"service.html",context) 
def skill(request):
   context={'skill':'active'}
   return render(request,"skill.html",context) 
def contact(request):
   context={'contact':'active'}
   return render(request,"contact.html",context) 
# Create your views here.
