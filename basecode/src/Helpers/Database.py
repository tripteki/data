import os
from typing import Dict, Any, Optional
from ...config.database import DB_DEFAULT, drivers
from asyncio import run
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

class database:

    def __init__ (self, plot: str = "async", space: Optional[str] = None, driver: Optional[str] = None) -> None:
        """
        :type space: Optional[str]
        :type driver: Optional[str]
        :rtype: None
        """

        """ :__plot: str """
        self.__plot = plot

        """ :__drivername: str """
        self.__drivername = driver

        """ :__driver: Dict """
        self.__driver = {}

        """ :__space: Dict """
        self.__space = {}

        """ :__connection: Any """
        self.__connection = None

        self.__loadDriver (driver)
        self.__loadSpace (space)

        self.__createConnection ()

    def __del__ (self) -> None:
        """
        :rtype: None
        """
        self.__destroyConnection ()

    def __loadDriver (self, driver: Optional[str] = None) -> None:
        """
        :type driver: Optional[str]
        :rtype: None
        :raises Exception:
        """
        if not driver:
            driver = DB_DEFAULT
            self.__drivername = driver

        driver = drivers.get (driver)

        if not driver:
            raise Exception ("Not the type of drivers")

        self.__driver = driver

    def __loadSpace (self, space: Optional[str] = None) -> None:
        """
        :type space: Optional[str]
        :rtype: None
        :raises Exception:
        """
        if not space:
            space = self.__driver.get ("default")
        else:
            space = self.__driver.get (space)

        if not space:
            raise Exception ("Not the type of spaces")

        self.__space = space

    def __createConnection (self) -> None:
        """
        :rtype: None
        :raises Exception:
        """
        url = ""

        if self.__drivername == "sqlite":
            database = self.__space.get ("database")

            if self.__plot == "sync":
                url = f"sqlite:///{database}"
            elif self.__plot == "async":
                url = f"sqlite+aiosqlite:///{database}"
        else:
            username = self.__space.get ("username")
            password = self.__space.get ("password")
            host = self.__space.get ("host")
            port = self.__space.get ("port")
            database = self.__space.get ("database")
            url = f"//{username}:{password}@{host}:{port}/{database}?charset=utf8"

            if self.__drivername == "mysql":
                if self.__plot == "sync":
                    url = f"mysql+pymysql:{url}"
                elif self.__plot == "async":
                    url = f"mysql+asyncmy:{url}"
            elif self.__drivername == "postgresql":
                if self.__plot == "sync":
                    url = f"postgresql+pygresql:{url}"
                elif self.__plot == "async":
                    url = f"postgresql+asyncpg:{url}"
            elif self.__drivername == "mssql":
                if self.__plot == "sync":
                    url = f"mssql+pymssql:{url}"
                elif self.__plot == "async":
                    raise Exception ("Currently not supported yet async in this driver")

        debug = False if os.environ.get ("PYTHON_ENV", "production") == "production" else True

        if self.__plot == "sync":
            self.__connection = create_engine (url, echo = debug)
        elif self.__plot == "async":
            self.__connection = create_async_engine (url, echo = debug, future = True)

    def __destroyConnection (self) -> None:
        """
        :rtype: None
        """
        if self.__connection:
            if self.__plot == "async":
                async def _ () -> None:
                    await self.__connection.dispose ()
                run (_ ())

            self.__connection = None

    def driver (self) -> Any:
        """
        :rtype: Any
        """
        return self.__connection

    def sql (self) -> Any:
        """
        :rtype: Any
        """
        return sessionmaker (self.driver (), expire_on_commit = False, class_ = AsyncSession)
