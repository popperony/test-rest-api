from rest_framework import serializers

from server.apps.palette.models import Palette, Color


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = (
            'id',
            'name',
            'created',
        )


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'id',
            'palette',
            'hex_code',
            'name',
        )

        read_only_fields = (
            'id',
            'name',
        )
