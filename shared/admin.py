from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin_

from .models import Client, User


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin_):
    pass
