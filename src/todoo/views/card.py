from rest_framework.viewsets import ModelViewSet

from ..models import Card
from ..serializers import (
    ListCardSerializer, CreateCardSerializer, UpdateCardSerializer,
)


class CardView(ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')
    list_serializer_class = ListCardSerializer
    create_serializer_class = CreateCardSerializer
    update_serialzier_class = UpdateCardSerializer
    queryset = Card.objects.all().order_by(
        '-created_at'
    ).select_related('category')

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(user=user)
        return super().get_queryset()

    def get_serializer_class(self):
        actions = {
            'create': self.create_serializer_class,
            'update': self.update_serialzier_class,
            'list': self.list_serializer_class,
        }
        return actions[self.action]
