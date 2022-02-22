from django.contrib import admin
from .models import User,UserEvents
# Register your models here.
admin.site.register(User)
admin.site.register(UserEvents)