import os
import datetime
from typing import Optional
from .BasePath import base_path

def log_name_space (space: Optional[str] = "") -> str:
    """
    :type space: Optional[str]
    :rtype: str
    """
    if os.environ.get ("PYTHON_ENV", "production") == "production":
        if space == "/":
            return "logs"
        else:
            return "logs/" + space + "/" + datetime.datetime.now ().strftime ("%d%m%Y%H%M%S") + ".log"
    else:
        if space == "/":
            return base_path ("logs")
        else:
            return base_path ("logs/" + space + "/" + datetime.datetime.now ().strftime ("%d%m%Y%H%M%S") + ".log")
