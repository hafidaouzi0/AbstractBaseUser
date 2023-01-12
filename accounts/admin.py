from django.contrib import admin
from django.contrib.auth import get_user_model
#from .models import CustomUser
# Register your models here.

user=get_user_model()
admin.site.register(user)
#admin.site.register(CustomUser)