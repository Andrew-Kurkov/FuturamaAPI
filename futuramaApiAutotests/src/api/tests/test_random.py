from src.api.clients.random import get_random_character, get_random_season, get_random_episode
from src.api.helpers.api_client import get_client


class TestRandom:
    client = get_client()
    def test_random_character(self):
        """Нахождение случайного персонажа"""
        response = get_random_character(self.client)
        assert response.status_code == 200
    def test_random_episode(self):
        """Нахождение случайный эпизод"""
        response = get_random_episode(self.client)
        assert response.status_code == 200
    def test_random_season(self):
        """Нахождение случайный сезон"""
        response = get_random_season(self.client)
        assert response.status_code == 200









