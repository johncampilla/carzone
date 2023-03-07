from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def carphoto(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.car_photo.url))
    
    carphoto.short_description='Photo'

    list_display=('id','car_title','carphoto','model','color','price','fuel_type', 'is_featured')
    list_display_links = ('id', 'car_title', 'carphoto')
    search_fields = ('car_title','model','fuel_type')
    list_filter = ('model','fuel_type')

    list_editable = ('is_featured',)

admin.site.register(Car, CarAdmin)
