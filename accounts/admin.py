from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser
# Register your models here.

user=get_user_model()



#this custom form concerns the admin dashboard 
class UserAdmin(admin.ModelAdmin):
    search_fields=['email','full_name']
    list_display=['email','full_name','admin']
    class Meta:
      model=user
      


admin.site.register(user,UserAdmin)
#admin.site.register(CustomUser)



