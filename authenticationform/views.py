from django.shortcuts import render,redirect
from .models import My_User
from .models import My_post
from django.contrib import auth

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
    u=My_User( first_name=fn, last_name=ln, mail=emid, password=pawd, user_name=usrnm )
    u.save()
    
    return render(request,'done.html')

def second(request):
    return render(request,'login.html')

#for user authentication
def Login(request):
    
    usernme=request.POST['usrnme']
    pswd=request.POST['pwd']
    
    v=auth.authenticate(user_name=usernme,  password=pswd)
    
    return render(request,'loginsuccess.html')
   

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




