from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import *

admin.register(User, auth_admin.UserAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    prepopulated_fields = {"username": ("email",)}
