from django.test import Client
from django.urls import reverse
from requests import Response


class TestLogin:
    @staticmethod
    def __send_request(data: dict, client: Client) -> Response:
        path = reverse(viewname='login')
        response: Response = client.post(
            path=path, data=data, content_type='application/json',
        )
        return response

    def test_success(self, db, user, client: Client) -> None:
        data = {
            'mail': 'test-mail@mail.com',
            'password': 'secret',
        }
        response = self.__send_request(data=data, client=client)
        assert response.status_code == 201
        body = response.json()
        assert body['token'] is not None

    def test_login_failure(self, db, client: Client) -> None:
        data = {
            'mail': 'test-mail@mail.com',
            'password': 'wrong_password',
        }
        response = self.__send_request(data=data, client=client)
        assert response.status_code == 401




