from django.shortcuts import render
from .models import My_User
from .models import My_post

# Create your views here.

def firstpage(request):
     return render(request,'user.html')
    
def register(request):
    
    fn=request.POST.get('Fname')
    ln=request.POST.get('Lname')
    emid=request.POST.get('email')
    pawd=request.POST.get('pwd')
    usrnm=request.POST.get('usrnm')
    u=My_User( first_name=fn, last_name=ln, mail=emid, password=pawd, user_name=usrnm )
    u.save()
    
    return render(request,'done.html')


def secondpage(request):
    return render(request,'post.html')

def posttext(request):
    
    txt=request.POST.get('myrecentpost')
    credt=request.POST.get('nowdate')
    updt=request.POST.get('updateddate')
    p=My_post( Text=txt,  created_date=credt, updated_date=updt )
    p.save()

    return render(request,'posted.html')




