from django.test import Client
from django.urls import reverse

from todoo.models import Category, Card


class TestCard:
    def test_create_card(
            self, db, authorized_client: Client, category: Category
    ) -> None:
        path = reverse(viewname='cards-list')
        data = {
            'name': 'new_card', 'category': category.pk
        }
        response = authorized_client.post(
            path=path, data=data, content_type='application/json'
        )
        assert response.status_code == 201
        card_id = response.json()['pk']
        assert Card.objects.get(pk=card_id)

    def test_update_card(
            self, db, authorized_client: Client, card: Card,
            category: Category,
    ) -> None:
        path = reverse(viewname='cards-detail', kwargs={'pk': card.pk})
        data = {
            'name': 'new_card', 'category': category.pk,
        }
        response = authorized_client.put(
            path=path, data=data, content_type='application/json'
        )
        print(response.json())
        assert response.status_code == 200
        card.refresh_from_db()
        assert card.name == data['name']

    def test_delete_card(
            self, db, authorized_client: Client, card: Card,
    ) -> None:
        path = reverse(viewname='cards-detail', kwargs={'pk': card.pk})
        response = authorized_client.delete(path=path)
        assert response.status_code == 204
        card.refresh_from_db()
        assert card.is_deleted

    def test_list_card(
            self, db, cards, authorized_client,
    ):
        path = reverse(viewname='cards-list')
        response = authorized_client.get(path=path)
        assert response.status_code == 200
        assert len(response.json()['results']) > 0
