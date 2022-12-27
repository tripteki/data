from typing import Any
from abc import ABC, abstractmethod
from ...src.Helpers.Database import database
from sqlalchemy import MetaData

class IMigration (ABC):

    def __init__ (self) -> None:
        """
        :rtype: None
        """

        """ :driver: Any """
        self.driver = database ("sync").driver ()

        """ :metadata: Any """
        self.metadata = MetaData ()

    def __del__ (self) -> None:
        """
        :rtype: None
        """
        self.metadata = None
        self.driver = None

    @abstractmethod
    def up (self) -> None:
        """
        :rtype: None
        """
        pass

    @abstractmethod
    def down (self) -> None:
        """
        :rtype: None
        """
        pass
