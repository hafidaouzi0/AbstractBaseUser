from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    #full_name = models.CharField(max_length=255,null=True,blank=True)
    active= models.BooleanField(default=True)  #can login
    staff= models.BooleanField(default=False) #staff non super user
    admin = models.BooleanField(default=False)#super user
    timestamp= models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD='email'
    #USERNAME_FIELD and password are required by defult 
    REQUIRED_FIELDS=[] #will berequired while : python manage.py createsuperuser
#ok

    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email

#CustomUser.active is the same as CustomerUser.is_admin
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_admin(self):
        return self.admin

