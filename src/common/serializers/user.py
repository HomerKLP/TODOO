from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


class ObtainTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True, max_length=64,
    )
    password = serializers.CharField(
        write_only=True, max_length=128,
    )
    token = serializers.CharField(
        source='key', read_only=True,
    )

    class Meta:
        model = Token
        fields = ('username', 'password', 'token',)

    def create(self, validated_data):
        user = authenticate(**validated_data)
        if not user:
            raise AuthenticationFailed(
                detail=_('Invalid credentials'), code='INVALID_CREDENTIALS',
            )
        return super().create({'user': user})
