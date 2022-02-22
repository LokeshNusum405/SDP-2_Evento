from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve

from . import views

urlpatterns = [

    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('bookevent/', views.bookevent, name="bookevent"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('deleteevent/<str:name>/<str:eventname>', views.deleteevent, name="deleteevent"),
    path('updateevent/<str:name>/<str:eventname>', views.updateevent, name="updateevent"),
    path('updateeventdetails/', views.updateeventdetails, name="updateeventdetails"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
