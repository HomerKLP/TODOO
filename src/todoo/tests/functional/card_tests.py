from django.test import Client
from django.urls import reverse

from todoo.models import Category


class TestCard:
    def test_create_card(
            self, db, authroized_client: Client, category: Category
    ) -> None:
        path = reverse(viewname='cards-list')
        data = {
            'name': 'new_card', 'category': category.pk
        }
        response = authroized_client.post(path=path, data=data)
        assert response.status_code == 201
        card_id = response.json()['pk']
        assert Card.objects.get(pk=card_id)

    def test_update_card(
            self, db, authroized_client: Client, card: Card,
    ) -> None:
        path = reverse(viewname='cards-detail', kwargs={'pk': card.pk})
        data = {'name': 'changed_name'}
        response = authroized_client.put(path=path, data=data)
        assert response.status_code == 200
        card.refresh_from_db()
        assert card.name == data['name']

    def test_delete_card(
            self, db, authroized_client: Client, card: Card,
    ) -> None:
        path = reverse(viewname='cards-detail', kwargs={'pk': card.pk})
        response = authroized_client.delete(path=path)
        assert response.status_code == 204
        card.refresh_from_db()
        assert card.is_deleted
