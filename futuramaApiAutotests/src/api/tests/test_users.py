import os

from src.api.clients.token import get_token, refresh_token
from src.api.clients.usres import get_users_list, post_users, get_user_info
from src.api.helpers.api_client import get_client


class TestUsers:
    client = get_client()
    def test_get_users_list(self):
        """Получение списка пользователей"""
        response = get_users_list(self.client)
        assert response.status_code == 200
    def test_create_user(self):
        """Создание пользователя"""
        response = post_users(self.client,name="yayayaya",surname="yoyoyoyo",middle_name="mc",email="pigion@shavala.cat",username="EmmEmmEp",password="12345678")
        assert response.status_code == 201 or response.status_code == 409
    def test_get_user_info(self):
        """Получение информации о пользователе"""
        response_token = get_token(self.client, username=os.getenv("username_EP"), password=os.getenv("password_EP"))
        response = get_user_info(self.client, access_token=response_token.json()['access_token'])
        print(self.client.base_url)
        assert response.status_code == 200
    def test_change_user_info(self):
        """Смена данных о пользователе"""
        new_name = "change_name"
        new_surname = "change_surname"
        response_token = get_token(self.client, username=os.getenv("username_EP"), password=os.getenv("password_EP"))
        response = change_user_info(self.client, access_token=response_token.json()['access_token'],name=new_name,Surname=new_surname)
        assert response.status_code == 200
