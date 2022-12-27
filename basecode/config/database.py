import os
from dotenv import load_dotenv
from ..src.Helpers.DatabaseNameSpace import database_name_space

load_dotenv ()



DB_DEFAULT = os.environ.get ("DB_DEFAULT", "sqlite")



drivers = {

    "sqlite": {

        "default": {

            "database": os.environ.get ("DB_DATABASE", database_name_space ("database.sqlite"))
        }
    },

    "mysql": {

        "default": {

            "host": os.environ.get ("DB_HOST", "localhost"),
            "port": os.environ.get ("DB_PORT", "3306"),
            "database": os.environ.get ("DB_DATABASE", "database"),
            "username": os.environ.get ("DB_USERNAME", "user"),
            "password": os.environ.get ("DB_PASSWORD", "password")
        }
    },

    "postgresql": {

        "default": {

            "host": os.environ.get ("DB_HOST", "localhost"),
            "port": os.environ.get ("DB_PORT", "5432"),
            "database": os.environ.get ("DB_DATABASE", "database"),
            "username": os.environ.get ("DB_USERNAME", "user"),
            "password": os.environ.get ("DB_PASSWORD", "password")
        }
    },

    "mssql": {

        "default": {

            "host": os.environ.get ("DB_HOST", "localhost"),
            "port": os.environ.get ("DB_PORT", "1433"),
            "database": os.environ.get ("DB_DATABASE", "database"),
            "username": os.environ.get ("DB_USERNAME", "user"),
            "password": os.environ.get ("DB_PASSWORD", "password")
        }
    }
}
