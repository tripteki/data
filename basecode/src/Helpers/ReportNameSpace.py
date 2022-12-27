import os
import datetime
from typing import Optional
from .BasePath import base_path

def report_name_space (space: Optional[str] = "") -> str:
    """
    :type space: Optional[str]
    :rtype: str
    """
    if os.environ.get ("PYTHON_ENV", "production") == "production":
        if space == "/":
            return "logs/reports"
        else:
            return "logs/reports/" + space + "/" + datetime.datetime.now ().strftime ("%d%m%Y%H%M%S") + ".html"
    else:
        if space == "/":
            return base_path ("logs/reports")
        else:
            return base_path ("logs/reports/" + space + "/" + datetime.datetime.now ().strftime ("%d%m%Y%H%M%S") + ".html")
