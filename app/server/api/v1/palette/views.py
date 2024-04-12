from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from server.api.v1.palette.serializers import PaletteSerializer, ColorSerializer
from server.apps.palette.models import Palette, Color


class PaletteViewSet(viewsets.ModelViewSet):
    """
    Методы для работы с палитрами:
    получение коллекции палитр,
    получение палитры по идентификатору,
    создание палитры,
    изменение палитры,
    удаление палитры.
    """
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, is_visible=True)


class ColorViewSet(viewsets.ModelViewSet):
    """
     Методы для работы с цветами:
     получение коллекции цветов по идентификатору палитры,
     получение цвета по идентификатору,
     создание цвета,
     изменение цвета,
     удаление цвета
    """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(palette__user=self.request.user)


class ColorsFromPaletteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, palette_id):
        if palette := Palette.objects.filter(id=palette_id, user=request.user, is_visible=True).first():
            colors = palette.color_set.all()
            serializer = ColorSerializer(colors, many=True)
            return Response(serializer.data)

        return Response({'error': 'Не найдено палитры с таким идентификатором'}, status=status.HTTP_404_NOT_FOUND)


