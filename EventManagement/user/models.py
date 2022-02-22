from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=20,default='',blank=False)
    lname = models.CharField(max_length=20, default='', blank=False)
    email = models.CharField(max_length=20, default='', blank=False)
    mobile = models.CharField(max_length=20, default='', blank=False)
    address = models.CharField(max_length=20, default='', blank=False)



class UserEvents(models.Model):
    name = models.CharField(max_length=100,blank=False)
    eventname = models.CharField(max_length=200,  blank=False)
    email = models.EmailField(max_length=200,  blank=False)
    date = models.DateField(auto_now_add=False , auto_now=False,blank=True)
    mobile = models.CharField(max_length=200,  blank=False)
    altmobile = models.CharField(max_length=200,  blank=False)


    amount = models.CharField(max_length=100,blank=False)

    description = models.CharField(max_length=200, default='', blank=False)
