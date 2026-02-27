from abc import ABC, abstractmethod
from types import AsyncGeneratorType
from typing import Union, Any

from berga_crawler.crawler.item import Item
from berga_crawler.crawler.request import Request
from berga_crawler.crawler.response import Response


class ItemParser(ABC):
    def __init__(self, crawler: Any) -> None:
        self.crawler = crawler
        self.follow = crawler.follow

    @abstractmethod
    async def parse_item(
        self, request: Request, response: Response, *args, **kwargs
    ) -> Union[Item, AsyncGeneratorType]:
        raise NotImplementedError("Not Implemented")
