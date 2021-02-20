from rest_framework import serializers

from todoo.models import Category


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Category
        fields = ('pk', 'name', 'user')
