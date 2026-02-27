from berga_crawler.crawler.request import Request


class RetryRequestException(Exception):
    """Exception raised when a request should be retried."""

    def __init__(self, request: Request, *args: object) -> None:
        self.request = request
        super().__init__(*args)


class RobotsBlockedException(Exception):
    """Exception raised when a request is blocked by robots.txt."""

    def __init__(self, url: str, *args: object) -> None:
        self.url = url
        super().__init__(*args)
