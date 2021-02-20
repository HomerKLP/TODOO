from django.test import Client
from django.urls import reverse


class TestCategory:
    def test_create_category(self, db, authorized_client: Client) -> None:
        path = reverse(viewname='category-list')
        data = {'name': 'new_category'}
        response = authorized_client.post(path=path, data=data)
        assert response.status_code == 201
        body = response.json()
        category_id = body['id']
        assert Category.objects.get(pk=category_id)

    def test_update_category(
            self, db, authorized_client: Client, category: Category,
    ) -> None:
        path = reverse(viewname='category-detail', kwargs={'pk': category.pk})
        data = {'name': 'new_category_name'}
        response = authorized_client.put(path=path, data=data)
        assert response.status_code == 200
        category = Category.objects.get(pk=category.pk)
        assert category.name == data['name']

    def test_delete_category(
            self, db, authorized_client: Client, category: Category,
    ):
        path = reverse(viewname='category-detail', kwargs={'pk': category.pk})
        response = authorized_client.delete(path=path)
        assert response.status_code == 200
        assert category.is_deleted
