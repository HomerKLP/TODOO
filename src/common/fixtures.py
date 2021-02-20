from pytest import fixture

from common.models import ExtendedUser


@fixture
def user() -> ExtendedUser:
    return ExtendedUser.objects.create_user(
        username='test-mail@mail.com', password='secret',
    )
