from django.shortcuts import render, redirect
from Shopello.models import Cities
from django.contrib import messages
# Create your views here.

def create(request):
    return render(request,'cities/create.html')

def createCity(request):
    return render(request,'cities/create.html')  

def store(request):
    city =Cities()
    city.cityName = request.POST.get('cityName')
    city.save()
    messages.success(request, "City Added Successfully")
    return render(request,'cities/create.html')

def index(request):
    cities = Cities.objects.raw('SELECT * FROM shopello_cities WHERE status IS NULL')
    return render(request, 'cities/index.html',{'cities':cities})

def updateView(request,pk):
    city = Cities.objects.get(id=pk)
    return render(request,'cities/edit.html',{'city':city})

def update(request,pk):
    city = Cities.objects.get(id=pk)
    city.cityName =request.POST.get('cityName')
    city.save()
    messages.success(request, "City Update Successfully")
    return redirect('/cities')

def delete(request,pk):
    city = Cities.objects.get(id=pk)
    city.status= "delected"
    city.save()
    messages.success(request,"City Deleted Successfully")
    return redirect('/cities')