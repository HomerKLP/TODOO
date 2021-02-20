from django.test import Client
from pytest import fixture
from rest_framework.authtoken.models import Token

from common.models import ExtendedUser


@fixture
def user() -> ExtendedUser:
    return ExtendedUser.objects.create_user(
        username='test-mail@mail.com', password='secret',
    )


@fixture
def authorized_client(user, client: Client) -> Client:
    token = Token.objects.create(user=user)
    client.defaults['HTTP_AUTHORIZATION'] = f'Token {token}'
    return client
