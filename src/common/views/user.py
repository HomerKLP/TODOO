from rest_framework.viewsets import ModelViewSet

from common.serializers import ObtainTokenSerializer


class ObtainTokenView(ModelViewSet):
    http_method_names = ('post', )
    serializer_class = ObtainTokenSerializer
    permission_classes = ()
