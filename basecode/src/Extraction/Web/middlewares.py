from typing import Any
from scrapy import signals
from itemadapter import is_item, ItemAdapter

class Middleware:

    @classmethod
    def from_crawler (cls, crawler: Any) -> Any:
        """
        :type crawler: Any
        :rtype: Any
        """
        instance = cls ()

        crawler.signals.connect (instance.spider_opened, signal = signals.spider_opened)

        return instance

    def process_spider_input (self, response: Any, spider: Any) -> None:
        """
        :type response: Any
        :type spider: Any
        :rtype: None
        """
        return None

    def process_spider_output (self, response: Any, result: Any, spider: Any) -> None:
        """
        :type response: Any
        :type result: Any
        :type spider: Any
        :rtype: None
        """
        for i in result:
            yield i

    def process_spider_exception (self, response: Any, exception: Any, spider: Any) -> None:
        """
        :type response: Any
        :type exception: Any
        :type spider: Any
        :rtype: None
        """
        pass

    def process_start_requests (self, start_requests: Any, spider: Any) -> None:
        """
        :type start_requests: Any
        :type spider: Any
        :rtype: None
        """
        for r in start_requests:
            yield r

    def process_finish_responses (self, finish_responses: Any, spider: Any) -> Any:
        """
        :type finish_responses: Any
        :type spider: Any
        :rtype: Any
        """
        pass

    def spider_opened (self, spider: Any) -> None:
        """
        :type spider: Any
        :rtype: None
        """
        spider.logger.info ("%s" % spider.name)

class DownloaderMiddleware:

    @classmethod
    def from_crawler (cls, crawler: Any) -> Any:
        """
        :type crawler: Any
        :rtype: Any
        """
        instance = cls ()

        crawler.signals.connect (instance.spider_opened, signal = signals.spider_opened)

        return instance

    def process_request (self, request: Any, spider: Any) -> None:
        """
        :type request: Any
        :type spider: Any
        :rtype: None
        """
        return None

    def process_response (self, request: Any, response: Any, spider: Any) -> Any:
        """
        :type request: Any
        :type spider: Any
        :rtype: Any
        """
        return response

    def process_exception (self, request: Any, exception: Any, spider: Any) -> None:
        """
        :type request: Any
        :type exception: Any
        :type spider: Any
        :rtype: None
        """
        pass

    def spider_opened (self, spider: Any) -> None:
        """
        :type spider: Any
        :rtype: None
        """
        spider.logger.info ("%s" % spider.name)
