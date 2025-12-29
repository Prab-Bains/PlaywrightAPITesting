from playwright.sync_api import APIRequestContext, Playwright

class APIClient:
    def __init__(self, playwright: Playwright, base_url: str, headers: dict | None = None):
        self._context: APIRequestContext = playwright.request.new_context(
            base_url=base_url,
            extra_http_headers=headers
        )

    def get(self, url: str, **kwargs):
        return self._context.get(url, **kwargs)

    def post(self, url: str, **kwargs):
        return self._context.post(url, **kwargs)

    def patch(self, url: str, **kwargs):
        return self._context.patch(url, **kwargs)

    def delete(self, url: str, **kwargs):
        return self._context.delete(url, **kwargs)

    def dispose(self):
        self._context.dispose()
