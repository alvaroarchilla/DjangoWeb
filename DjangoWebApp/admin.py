from django.contrib import admin
from .models import Bug

# Register your models here.
class BugAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')



admin.site.register(Bug, BugAdmin)