import os

from src.api.clients.token import get_token, refresh_token
from src.api.helpers.api_client import get_client


class TestToken:
    client = get_client()
    def test_get_token(self):
        """Получение токена авторизации"""
        response = get_token(self.client, username=os.getenv("username_EP"), password=os.getenv("password_EP"))
        print(response.json()['access_token'])
        assert response.status_code == 200

    def test_refresh_token(self):
        """Обновление токена авторизации"""
        response_token = get_token(self.client, username=os.getenv("username_EP"), password=os.getenv("password_EP"))
        response = refresh_token(self.client,refresh_token=response_token.json()['refresh_token'])
        print(response_token.json())
        assert response.status_code == 200