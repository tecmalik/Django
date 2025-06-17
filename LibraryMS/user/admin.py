

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import Author, User


# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_per_page = 10



@admin.register(Author)
class AuthorAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2", "first_name", "last_name", "email","phone","dob", "dod"),
            },
        ),
    )
    list_display = ['first_name', 'last_name', 'email','phone','dob', 'dod']
    list_display_links = [ 'email','dob', 'dod']
    list_editable = ['first_name', 'last_name', 'phone']


# admin.site.register(Author)