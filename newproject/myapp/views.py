
from django.shortcuts import render, redirect
from .models import Food,Food_consume
from django.contrib.auth.models import User,auth
from django.contrib import messages

def loadLogin(request):
    return render(request,"Login.html")

def loadFood(request):
    return render(request,"Food.html")

def addFood(request):
    if request.method=="POST":
        vfname = request.POST.get('fname')
        vcarb=request.POST.get('carb')
        vfat = request.POST.get('fat')
        vpro = request.POST.get('pro')
        vcal = request.POST.get('cal')
        obj=Food()
        obj.name=vfname
        obj.carbs=vcarb
        obj.fats=vfat
        obj.protein=vpro
        obj.calories=vcal
        obj.save()
        return redirect('/index')
    else:
        return redirect('/loadfood')

def Index(request):
    if request.method=='POST':
        vfood_consumed=request.POST.get('food_consume')
        consume=Food.objects.get(name=vfood_consumed)
        vuser=request.user
        food_consume=Food_consume(user=vuser,food_consume=consume)
        food_consume.save()
        food_item=Food.objects.all()
    else:
        food_item=Food.objects.all()
    food_selected=Food_consume.objects.filter(user=request.user)
    return render(request, 'Index.html',{'food':food_item,'food_item':food_selected})

def delFood(request,fid):
    consume_food=Food_consume.objects.get(id=fid)
    consume_food.delete()
    return redirect ('/index')

def userlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpass = request.POST.get('pass')
        newuser=auth.authenticate(username=vuname,password=vpass)
        if newuser is not None:
            auth.login(request,newuser)
            return redirect('/index')

        else:
            messages.success(request, "Kindly Provide correct Username and Password")
            return redirect('/')

# Create your models here.
