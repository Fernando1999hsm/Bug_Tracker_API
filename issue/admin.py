from django.contrib import admin
from .models import Issue, Application

# Register your models here.
admin.site.register(Issue)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
