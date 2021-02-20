from pytest import fixture

from common.models import ExtendedUser
from todoo.models import Category


@fixture
def category(user: ExtendedUser) -> Category:
    return Category.objects.create(name='test_category', user=user)
