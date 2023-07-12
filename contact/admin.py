from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']
    date_hierarchy = 'created_date'
    search_fields = ['name', 'email', 'subject']


admin.site.register(Contact, ContactAdmin)
