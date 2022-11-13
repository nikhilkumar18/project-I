from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  auth,User
from django.contrib import  messages
from .models import jobs
 
from .filters import jobsfilter




def index(request):
    job =jobs.objects.all()
    #  for filtering
    jobs_filter = jobsfilter(request.GET , queryset = job)
    context = {'jobs_filter' : jobs_filter}
     
    return render(request,"index.html",{'jobs':job , 'context':context})
 

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect("/")
        else:
            messages.info(request,'Credentials invalid')
            return redirect(login)
    else:
        return render(request,'login.html')


def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1=='' or password2=='':
            messages.info(request,'Requires password')
            return redirect(signup)
        elif email=='':
            messages.info(request,'Requires email')
            return redirect(signup)
        elif username=='':
            messages.info(request,'Requires username')
            return redirect(signup)    
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect(signup)
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect(signup)
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect(login)
        else:
            messages.info(request,'Passwords not matching')
            return redirect(login)
    else:        
        return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def jobfunc(request,pk):
    job = jobs.objects.get(id=pk)
    return render(request,'jobfunc.html',{'jobs': job})


def reviews(request):
    return render(request,'reviews.html')


def contact(request):
    return render(request,'contact.html')


def jobsfilterdata(request):
    job = jobs.objects.all()
    jobs_filter = jobsfilter(request.GET , queryset = job)
    context = {'jobs_filter' : jobs_filter}
    return render(request,'index.html', context )
    # model = jobs

    # def get_data(self,**kargs):
    #     context = super().get_data(**kargs)
    #     context['filter']  = jobsfilter(self.request.GET , queryset = self.)
