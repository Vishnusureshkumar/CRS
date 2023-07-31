from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages,auth
from .forms import NewUserForm

from .models import *
# Create your views here.
def About(request):
    return render(request,'about.html')

def Home(request):
    return render(request,'home.html')


def Contact(request):
    return render(request,'contact.html')


def Useri(request):
    return render(request,'useri.html')

def regcomplaints(request):
    if request.method == "POST":
        data =request.POST
        name=data.get('name')
        flatblock=data.get('flatblock')
        flatno=data.get('flatno')
        date=data.get('date')
        email=data.get('email')
        phoneno=data.get('phoneno')
        complainttitle=data.get('complainttitle')
        complaintdescription=data.get('complaintdescription')
        complaintmedia=request.FILES.get('complaintmedia')
        
        Regcomplaint.objects.create(
            name=name,
            flatblock=flatblock,
            flatno=flatno,
            date=date,
            email=email,
            phoneno=phoneno,
            complainttitle=complainttitle,
            complaintdescription=complaintdescription,
            complaintmedia=complaintmedia,
        )
        return redirect('/regcomplaints/')
    queryset =Regcomplaint.objects.all()
    context ={'regcomplaints':queryset}  
    
    return render(request,'regcomplaints.html',context)

def Viewstatcomplaints(request):
    queryset =Regcomplaint.objects.all()
    context ={'regcomplaints':queryset}  
    
    return render(request,'viewstatcomplaints.html',context)

def Feedcomplaints(request):
    return render(request,'feedcomplaints.html')

def Staffdash(request):
    return render(request,'staffdash.html')
def Viewcomplaints(request):
    return render(request,'viewcomplaints.html')  

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def Adduser(request):
    if request.method == "POST":
        data =request.POST
        name=data.get('name')
        email=data.get('email')
        image=request.FILES.get('image')
        
        Addmember.objects.create(
            name=name,
            email=email,
            image=image,
        )
        
    return render(request,'adduser.html') 

def Login(request):
    error = ""
    if request.method == "POST":
        u =request.POST['uname']
        p =request.POST['pwd']
        user =authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error ="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}        
    return render(request,'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('admin_login')




#user reg
def SignupPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"signup Successfull.")
            return redirect('logi')
    messages.error(request,"unsuccessfull registration.invalid information")
    form = NewUserForm()
    return render(request=request, template_name="user/signup.html", context={"register_form":form})
        
	
    #if request.method == "POST":
#        uname=request.POST.get('username')
#        email=request.POST.get('email')
#        pass1=request.POST.get('password1')
#        pass2=request.POST.get('password2')
#        if pass1!=pass2:
#            return HttpResponse("your password and confirm pass are not same.")
    #    my_user=User.objects.create_user(uname,email,pass1)
    #   my_user.save()
    #    return redirect('logi')
    
#    return render(request,'user/signup.html')



        
#staff login
def Login_govt(request):
    if request.method == "POST":
        username=request.POST.get('uname')
        pass1=request.POST.get('pwd')
        user=authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request,user)
            return redirect('staffdash')
        else:
            return redirect('loggvt')
    return render(request,'loggvt.html')




def LoginPage(request):   
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("useri")
            else:
                messages.error(request,"Invalid username or password.")
    else:
                messages.error(request,"Invalid username or password.")
                form = AuthenticationForm()
    return render(request=request, template_name="user/logi.html", context={"login_form":form})
   


def Logout_user(request):
    if request.user is not None:
        return redirect('logi')
    logout(request)
    return redirect('logi')





