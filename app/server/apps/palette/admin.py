from django.contrib import admin

from server.apps.palette.models import Palette, Color


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created'
    )
    list_display_links = list_display


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'palette',
        'hex_code',
        'name'
    )
    list_display_links = list_display
    list_filter = ('palette',)
    search_fields = (
        'name',
        'hex_code'
    )
    readonly_fields = ('name',)
