from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


def first(request):
    return redirect('register')


def userhome(request):
    return render(request,"userhome.html")

def aboutus(request):
    return render(request,"aboutus.html")

def moreevents(request):
    return render(request,"moreevents.html")



def logoutpage(request):
    logout(request)
    return redirect('login')
