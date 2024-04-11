from django.conf import settings


def get_app_list(self, request):
    """
    Переопределенный метод get_app_list сортировки приложений и моделей в Админке
    """
    app_dict = self._build_app_dict(request)
    for app_name, object_list in settings.ADMIN_ORDERING:
        app = app_dict.get(app_name)
        if app is not None:
            app['models'].sort(key=lambda x: object_list.index(x['object_name']))
            yield app
