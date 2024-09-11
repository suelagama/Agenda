from django.contrib import admin

from contact.models import Category, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'phone', 'created_date', 'show')
    ordering = '-id',
    readonly_fields = ('created_date',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'category')
        }),
        ('Additional Info', {
            'fields': ('description', 'picture', 'show', 'created_date', 'owner')
        }),
    )
    search_fields = 'first_name', 'last_name', 'phone', 'email'
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = 'first_name',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = '-id',
