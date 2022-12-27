from typing import Any
from .Contracts.IApi import IApi

class ApiData (IApi):

    """ :url: str """
    url = "http://localhost:80"

    def parse (self) -> Any:
        """
        :rtype: Any
        """
        pass
