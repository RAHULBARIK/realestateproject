from django.contrib import admin
from .models import Contact
# we need to import the model(Contact) from models for displaying in the admin section


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    # The things i need to display in my admin dashboard
    list_display_links = ('id', 'name')
    # The things that are clickable links so that admin can directly navigate to that page
    search_fields = ('name', 'email', 'listing')
    # The fields admin by its name,email or listing  need to search in admin dashboard
    list_per_page = 25
    # The number of rows of data in the date section

    # You should follow style of declaring the variables as it is the default class based views


admin.site.register(Contact, ContactAdmin)
# Register your models here.
