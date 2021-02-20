from rest_framework.viewsets import ModelViewSet

from todoo.models import Category
from todoo.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    http_method_names = ('post', 'put', 'delete')
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
