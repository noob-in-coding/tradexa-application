
from django.shortcuts import render,redirect
from .models import My_User
 
from .models import My_post
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist 

# Create your views here.

#to get user.html page
def firstpage(request):
     return render(request,'user.html')

#for storing data from html form in to the database that is created in My_User models   
def register(request):
    
    fn=request.POST.get('Fname')
    ln=request.POST.get('Lname')
    emid=request.POST.get('email')
    pawd=request.POST.get('pwd')
    usrnm=request.POST.get('usrnm')
    u=My_User( first_name=fn, last_name=ln, mail=emid, password=pawd, username=usrnm )
    u.save()
    
    return render(request,'done.html')

def second(request):
    return render(request,'login.html')



#for user authentication
def Login(request):
    if request.method == "POST" :
        username1=request.POST.get('usernm')
        password1=request.POST.get('passwd')
        user=authenticate(username=username1,password=password1)
        if user==True:
            login(request,user)
            return render(request,'login.html')
        else:
            return render(request,'log.html')

#to get post.html page
def secondpage(request):
    return render(request,'post.html')

#for storing data from html form in to the database that is created in My_post models
def posttext(request):
    
    txt=request.POST.get('myrecentpost')
    credt=request.POST.get('nowdate')
    updt=request.POST.get('updateddate')
    p=My_post( Text=txt,  created_date=credt, updated_date=updt )
    p.save()

    return render(request,'posted.html')




