from django.contrib import admin

from .models import ApplicationType, Application, ApplicationEntry


@admin.register(ApplicationType)
class ApplicationTypeAdmin(admin.ModelAdmin):
    pass


class ApplicationEntryAdmin(admin.TabularInline):
    model = ApplicationEntry


@admin.register(Application)
class ApplicationTypeAdmin(admin.ModelAdmin):
    inlines = (ApplicationEntryAdmin,)
