import os

import httpx
from dotenv import load_dotenv


def get_client(timeout: int = None):
    """Получение httpx-клиента

    :param timeout время ожидания от сервера
    """

    load_dotenv()
    return httpx.Client(base_url=os.getenv("BASE_URL"), timeout=timeout)