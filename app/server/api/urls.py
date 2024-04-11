from django.urls import path, include

app_name = 'api'  # pylint: disable=invalid-name

urlpatterns = [
    path('v1/', include('server.api.v1.urls', namespace='v1')),
]
