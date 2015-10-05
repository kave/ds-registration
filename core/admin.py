from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from . import models

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms


class RegisterAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Registration, RegisterAdmin)
