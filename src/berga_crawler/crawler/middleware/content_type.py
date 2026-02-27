from berga_crawler.crawler.middleware.base import BaseDownloaderMiddleware
from berga_crawler.crawler.request import Request
from berga_crawler.crawler.response import Response


class ContentTypeMiddleware(BaseDownloaderMiddleware):
    async def pre_request(self, request: Request) -> None:
        """Called before processing a request."""
        pass

    async def process_request(self, request: Request) -> None:
        """Called during request processing."""
        pass

    async def process_response(self, response: Response) -> None:
        # Downloader already handles most of this.
        # This middleware is currently a placeholder or can be used for extra processing.
        pass

    async def process_exception(self, request: Request, exception: Exception) -> None:
        """Called when an exception occurs during request processing."""
        pass
