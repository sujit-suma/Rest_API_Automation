import pytest
from playwright.sync_api import sync_playwright
from config.config import BASE_URL, HEADERS


@pytest.fixture(scope='session')
def request_context():
    with sync_playwright() as playwright:
        request_context = playwright.request.new_context(
            base_url=BASE_URL,
            extra_http_headers=HEADERS
        )
        yield request_context
        request_context.dispose()