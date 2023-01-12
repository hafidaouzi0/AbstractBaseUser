
from django.db import models

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
# Create your models here.


#that's how you create and save a user
class MyUserManager(BaseUserManager):
    #takes all the required fields as arguments
   def create_user(self,email,password=None,is_staff=False,is_admin=False,is_active=True):

    if not email:
        raise ValueError("Users must have an email adress")

    if not password:
        raise ValueError("Users must have a password")
    
    user_obj=self.model(
        email=self.normalize_email(email)
    )
    user_obj.set_password(password)
    user_obj.active=is_active
    user_obj.staff=is_staff
    user_obj.admin=is_admin
    user_obj.save(using=self._db)
    return user_obj

   def create_staff(self,email,password=None):
     user=self.create_user(
        email,
        password=password,
        is_staff=True
     )  
     return user
    
   def create_superuser(self,email,password=None):
       user=self.create_user(
        email,
        password=password,
        is_staff=True,
        is_admin=True
       )
       return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    #full_name = models.CharField(max_length=255,null=True,blank=True)
    active= models.BooleanField(default=True)  #can login
    staff= models.BooleanField(default=False) #staff non super user
    admin = models.BooleanField(default=False)#super user
    timestamp= models.DateTimeField(auto_now_add=True)

    objects=MyUserManager()

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


    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True


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

