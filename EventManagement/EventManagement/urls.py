
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first,name='first'),

    path('userhome/', views.userhome, name="userhome"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('moreevents/', views.moreevents, name="moreevents"),

    path('logout/',views.logoutpage,name="logout"),
    path("",include("user.urls")),
]
