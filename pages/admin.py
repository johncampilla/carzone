from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
    
    myphoto.short_description='Photo'

    
    list_display = ('id','myphoto','firstName','lastName','designation','created_date')
    list_display_links = ('id', 'myphoto', 'firstName', 'lastName')
    search_fields = ('firstName','lastName','designation')
    list_filter = ('designation',)



admin.site.register(Team, TeamAdmin)
