import pytest

from src.api.clients.characters import get_characters_list, get_character
from src.api.helpers.api_client import get_client


class TestCharacters:
    client = get_client()
    @pytest.mark.parametrize("character_id, character_name", [(1,"Philip J. Fry"),
                                                                (2,"Morgan Proctor"),
                                                                (3,"Mugger")])
    def test_get_character_by_id(self,character_id,character_name):
        """Проверка получения информации о персонаже по ИД."""
        response = get_character(self.client,character_id)
        assert response.status_code == 200
        assert response.json()["name"] == character_name
        assert response.json()["id"] == character_id

    def test_get_charaters_list(self):
        """Проверка получения списка персонажей"""
        response = get_characters_list(self.client)
        assert response.status_code == 200