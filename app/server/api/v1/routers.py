from rest_framework import routers

from server.api.v1.palette.views import PaletteViewSet, ColorViewSet
from server.api.v1.user.views import UserCreateViewSet, UserViewSets

router = routers.DefaultRouter()
router.register('register', UserCreateViewSet, basename='register')
router.register('user', UserViewSets, basename='user')
router.register('palette', PaletteViewSet, basename='palette')
router.register('color', ColorViewSet, basename='color')
