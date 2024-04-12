import requests
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from server.apps.palette.models import Color


@receiver(post_save, sender=Color)
def update_name_field_from_colorapi(sender, instance, **kwargs):
    url = settings.COLORAPI_URL
    response = requests.get(url, params={'hex': instance.hex_code})

    if response.status_code == 200:
        items = response.json()
        post_save.disconnect(update_name_field_from_colorapi, sender=Color)
        instance.name = items.get('name')['value']
        instance.save()
        post_save.connect(update_name_field_from_colorapi, sender=Color)
    return instance
