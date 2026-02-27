from typing import Dict, Any
from berga_crawler.crawler.middleware.base import BaseDownloaderMiddleware
from berga_crawler.crawler.request import Request
from berga_crawler.crawler.response import Response
from yarl import URL


class CookieMiddleware(BaseDownloaderMiddleware):
    def __init__(self) -> None:
        self.cookie_jar: Dict[str, Any] = {}

    async def pre_request(self, request: Request) -> None:
        """Called before processing a request."""
        pass

    async def process_request(self, request: Request) -> None:
        # Attach cookies for the domain
        domain = URL(request.url).host
        request.cookies = self.cookie_jar.get(domain, {})

    async def process_response(self, response: Response) -> None:
        # Store cookies from response
        domain = URL(response.url).host
        self.cookie_jar[domain] = response.cookies

    async def process_exception(self, request: Request, exception: Exception) -> None:
        """Called when an exception occurs during request processing."""
        pass
