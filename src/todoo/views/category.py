from rest_framework.viewsets import ModelViewSet

from ..models import Category
from ..serializers import CategorySerializer


class CategoryView(ModelViewSet):
    http_method_names = ('post', 'put', 'delete')
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
