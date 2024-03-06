from django.contrib import admin

from .models import Listify

class ListifyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    
admin.site.register(Listify, ListifyAdmin )
