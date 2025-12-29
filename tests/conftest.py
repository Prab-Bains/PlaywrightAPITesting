import pytest
from playwright.sync_api import sync_playwright
from utils.api_client import APIClient
from config.settings import BASE_URL

# Defines the setup and cleanup for every test
@pytest.fixture()
def api_client():
    with sync_playwright() as p:
        client = APIClient(p, BASE_URL)
        yield client
        client.dispose()
