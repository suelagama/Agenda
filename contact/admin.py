from django.contrib import admin

from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email'
    ordering = '-id',
    search_fields = 'first_name', 'last_name', 'phone', 'email'
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = 'first_name',
