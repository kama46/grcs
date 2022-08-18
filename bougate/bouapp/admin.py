from django.contrib import admin
from .models import Item, Person, Badge

# Creating a new Admin dashboard / Adding Another Admin Dashboard
from django.contrib.admin import AdminSite


class UserSite(AdminSite):
    site_header = "User"
    site_title = "User Manager"
    index_title = 'Welcome to User Portal'


# Defining Modules User can access
user_site = UserSite(name='user_portal')
user_site.register(Item)
user_site.register(Person)
user_site.register(Badge)


# Adding Item model to the Admin section/dashboard
# admin.site.register(Item)
# configuring what and to display Item attributes
@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('serial_number', 'item_name', 'type')
    ordering = ('serial_number',)
    search_fields = ('item_name', 'type')


# Adding Item_carrier model to the Admin section/dashboard
# admin.site.register(Item_carrier)
# configuring what and to display Item_carrier attributes

@admin.register(Person)
class Item_carrier(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'organisation', 'telephone', 'email')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name')


# Adding Badge model to the Admin section/dashboard
# admin.site.register(Badge)
# configuring what and to display Badge attributes
@admin.register(Badge)
class Badge(admin.ModelAdmin):
    list_display = ('item_name', 'time_in')
    ordering = ('time_in',)
    search_fields = ('item_name', 'time_in')
