from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from server.api.v1.palette.views import ColorsFromPaletteAPIView
from server.api.v1.routers import router
from server.api.v1.user.views import (
    DecoratedTokenObtainPairView,
)

app_name = 'v1'

urlpatterns = [
    path('login/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('color/<int:palette_id>/', ColorsFromPaletteAPIView.as_view(), name='palette-colors'),
]
