from config.settings import USERNAME, PASSWORD
from utils.api_client import APIClient


def login(api_client):
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "credentials": 'include'
    }

    response = api_client.post("/auth/login", data=payload)

    return response