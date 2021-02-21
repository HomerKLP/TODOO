from rest_framework import serializers

from ..models import Card, Category
from .category import CategorySerializer


class ListCardSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Card
        fields = ('pk', 'name', 'category')
        read_only_fields = fields


class CreateCardSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Card
        fields = ('pk', 'name', 'category', 'user')


class UpdateCardSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Category.objects.all(), allow_null=False,
    )

    class Meta:
        model = Card
        fields = ('pk', 'name', 'category')
