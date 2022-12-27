from typing import Any, List
from scrapy import Spider

class WebData (Spider):

    """ :name: str """
    name = "webdata"

    """ :allowed_domains: List[str] """
    allowed_domains = ["localhost"]

    """ :start_urls: List[str] """
    start_urls = ["http://localhost:80"]

    def parse (self, response: Any) -> Any:
        """
        :type response: Any
        :rtype: Any
        """
        pass
