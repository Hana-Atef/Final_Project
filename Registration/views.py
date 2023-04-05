from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Patient, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'patient.html')

def SignupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        # gender = request.POST.get('gender')
        # relation = request.POST.get('relation')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if password!=re_password:
            return HttpResponse("Your Password and conform password are not same")
        else:
            my_user= Profile.objects.create(username=username,fname=fname,lname=lname,email=email,password=password)
        my_user.save()
        return redirect ('login')
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('your_pass')
        parent = authenticate(request,username=username,password=password)
        if parent is not None:
            login(request,parent)
            return redirect('patient')
        else:
            return HttpResponse('Username or password is incorrect')
    
    return render (request,'login.html')


def patientPage(request):
    if request.method=='POST':
        patient_name = request.POST.get('patient_name')
        DoB = request.POST.get('DoB')
        my_patient= Patient.objects.create(patient_name=patient_name,DoB=DoB)
        my_patient.save()
        return redirect ('home')
    return render (request,'patient.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
