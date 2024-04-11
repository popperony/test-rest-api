from django.contrib import admin

from server.apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'date_joined')
    list_display_links = list_display


