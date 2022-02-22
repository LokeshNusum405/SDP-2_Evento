from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from .models import User,UserEvents


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, user + ' Created Account Successfully')
            subject = "Evento Registration"
            email = form.cleaned_data.get('email')  # to whom you want to send
            request.session['email'] = email
            email = EmailMessage(subject, " Hello 👋" + user+", You Successfully  Registered for Evento Website here is the link :    ",to=[email])  # to will take list of email IDs
            #email.send()
            messages.success(request,'Email Has been Sent to User '+user)
            response = HttpResponse("Cookie Demo")
            response.set_cookie('username', user)
            response.set_cookie('password', password)
            return redirect('login')


    context = {'form':form}
    return render(request, "register.html",context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('userhome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username = username ,password = password)

            if user is not None:
                login(request,user)
                request.session['username'] = username
                messages.success(request, username + ' Logged In Successfully')
                return redirect('userhome')
            else:
                messages.info(request , 'Username Or Password is Incorrect')

        context = {}
        return render(request, "login.html",context);

def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('adminhome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['username'] = username
                messages.success(request, username + ' Logged In Successfully')
                return redirect('adminhome')
            else:
                messages.info(request, 'Username Or Password is Incorrect')

        context = {}
        return render(request, "login.html", context);

def adminhome(request):
    bookedevents = UserEvents.objects.all()
    count = UserEvents.objects.all().count()
    return render(request,"adminhome.html",{ 'bookedevents':bookedevents,'count':count})

def myaccount(request):
    username = request.session['username']
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']

        user = User()
        user.fname = fname
        user.lname = lname
        user.email = email
        user.mobile = mobile
        user.address = address

        user.save()
        messages.success(request, ' Account Details Updated  Successfully ')
    return render(request,"myaccount.html",{'username':username })

def bookevent(request):
    username = request.session['username']
    #semail = request.session['email']
    if request.method == 'POST':
        name = request.POST.get('name')
        eventname = request.POST.get('eventname', False);
        email = request.POST.get('email', False);
        date = request.POST.get('date', False);
        mobile = request.POST.get('mobile', False);
        altmobile = request.POST.get('altmobile', False);
        amount = request.POST.get('amount',False);
        description = request.POST.get('description', False);
        print(name,eventname)
        eventbook = UserEvents()

        toname = eventbook.name = name
        toeventname = eventbook.eventname = eventname
        toemail = eventbook.email = email
        todate = eventbook.date = date
        tomobile = eventbook.mobile = mobile
        toaltmobile = eventbook.altmobile = altmobile
        toamount = eventbook.amount = amount
        todescription = eventbook.description = description

        eventbook.save()
        subject = "Event Booking"
        email = toemail  # to whom you want to send
        eventname = toeventname
        email = EmailMessage(subject,
                             " Hello " + username + ", You Successfully  Booked for a "+ eventname +" Event Our Event Managers Will Contact You Soon through mobile "
                                                                                                 " ### Booking Details ### "
                                                                                                 "Full Name : " + toname  +
                             "Event Name : " + toeventname +"Event Date : " + todate  +"Mobile : " + tomobile  + "Alt Mobile : " + toaltmobile  +
                             "Efforded Amount : " + toamount + "Description : " + todescription  +
                            "Stay Tune to More Updates Have a Great Day 😊    ",
                             to=[email])  # to will take list of email IDs
        email.send()
        messages.success(request, ' Event Booked Successfully we will Contact You soon through mail Stay Tuned :)')

    return render(request,"bookevent.html",{'username':username}  )


def deleteevent(request,name,eventname):
    username = request.session["username"]
    UserEvents.objects.filter(name=name,eventname=eventname).delete()
    messages.success(request, ' Event Deleted Successfully ')
    return redirect('adminhome')

def updateevent(request,name,eventname):
    username = request.session["username"]
    request.session["name"]= name
    request.session["eventname"] = eventname
    userevents = UserEvents.objects.filter(name=name, eventname=eventname)
    return render(request,'updateeventdetails.html',{'name':name , 'eventname' : eventname , })

def updateeventdetails(request):
    name = request.session["name"]
    eventname = request.session["eventname"]
    if request.method == 'POST':
        name = request.POST.get('name')
        eventname = request.POST.get('eventname', False);
        semail = request.POST.get('email', False);
        date = request.POST.get('date', False);
        mobile = request.POST.get('mobile', False);
        altmobile = request.POST.get('altmobile', False);
        amount = request.POST.get('amount', False);
        description = request.POST.get('description', False);
        print(name, eventname)
        UserEvents.objects.filter(name=name,eventname=eventname).update(email=semail,date=date,mobile=mobile,altmobile=altmobile,amount=amount,description=description)


        subject = "Event Booking"
        email = semail  # to whom you want to send
        email = EmailMessage(subject,
                             " Hello " + name + ", Your Booked Event is Updated by admin ,Once check ",
                             to=[email])  # to will take list of email IDs
        email.send()
        messages.success(request, ' Event Updated Successfully Check your Mail for Further Updates')

    return render(request, "adminhome.html", {'username': name})
