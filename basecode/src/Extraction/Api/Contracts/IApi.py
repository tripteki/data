import sys
import datetime
from typing import Any
from abc import ABC, abstractmethod

class IApi (ABC):

    def log (self) -> None:
        """
        :rtype: None
        """
        sys.stdout.write (str (datetime.datetime.now()) + " : " + self.__class__.__name__ + "\n")
        sys.stdout.flush ()

    @abstractmethod
    def parse (self) -> Any:
        """
        :rtype: Any
        """
        pass
