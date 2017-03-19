from django.contrib import admin

from .models import ApplicationType, Application, ApplicationEntry


@admin.register(ApplicationType)
class ApplicationTypeAdmin(admin.ModelAdmin):
    pass
