from common.models import ExtendedUser


def test_extended_user(db) -> None:
    ExtendedUser.objects.create_user(username='123')
    user: ExtendedUser = ExtendedUser.objects.get(username='123')
    assert user
    user.delete()
    assert user.is_deleted
