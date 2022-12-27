from .Contracts.IMigration import IMigration
from sqlalchemy import Table, Column, Integer, String

class User (IMigration):

    def up (self) -> None:
        """
        :rtype: None
        """
        Table (
            "users",
            self.metadata,
            Column ("id", Integer, primary_key = True),
            Column ("name", String (120))
        )

        self.metadata.create_all (self.driver, checkfirst = True)

    def down (self) -> None:
        """
        :rtype: None
        """
        Table (
            "users",
            self.metadata
        )

        self.metadata.drop_all (self.driver, checkfirst = True)
