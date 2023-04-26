from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserprofileAdmin(admin.ModelAdmin):
    list_display= ('email', 'name', 'is_active', 'is_staff')

admin.site.register(UserProfile)