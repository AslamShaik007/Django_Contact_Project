from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

class ContactAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'info',
        'gender',
        'image',
        'date_added',
    )
    list_display_links = (
        'id',
        'name'
    )
    list_editable = (
        'info',
        'gender',
    )
    list_per_page = 10
    search_fields = (
        'name',
        'info',
        'gender',
    )
    list_filter = (
        'name',
        'info',
        'gender',
    )

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
