import os
import datetime
from typing import Optional
from .ApplicationPath import application_path

def database_name_space (space: Optional[str] = None) -> str:
    """
    :type space: Optional[str]
    :rtype: str
    """
    if space:
        return application_path ("database/" + space)
    else:
        return application_path ("database")
