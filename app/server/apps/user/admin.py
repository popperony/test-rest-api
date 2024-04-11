from django.contrib import admin
from django.contrib.admin.models import LogEntry

from server.apps.user.models import User
from server.apps.user.utils import get_app_list

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'date_joined')
    list_display_links = list_display


admin.AdminSite.get_app_list = get_app_list
