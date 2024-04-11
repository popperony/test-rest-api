
class SerializerByAction:
    serializer_classes = {}

    def get_serializer_class(self, action=None):
        action = action or self.action
        return self.serializer_classes.get(action) or self.serializer_classes.get('default', self.serializer_class)

    def get_serializer(self, *args, action=None, **kwargs):
        serializer_class = self.get_serializer_class(action=action)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)