from pytest import fixture

from common.models import ExtendedUser
from todoo.models import Category, Card


@fixture
def category(user: ExtendedUser) -> Category:
    return Category.objects.create(name='test_category', user=user)


@fixture
def card(user: ExtendedUser, category: Category) -> Card:
    return Card.objects.create(category=category, user=user, name='test_card')


@fixture
def cards(user: ExtendedUser, category: Category) -> None:
    for _ in range(3):
        Card.objects.create(category=category, user=user, name='test_card')
