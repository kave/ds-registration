from django.contrib import admin
from . import models


class RegisterAdmin(admin.ModelAdmin):
    list_display = ("get_name", "email", "phone", "can_model", "create_date")


admin.site.register(models.Registration, RegisterAdmin)
