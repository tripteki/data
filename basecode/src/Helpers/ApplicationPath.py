from typing import Optional
from .BasePath import base_path

def application_path (path: Optional[str] = None) -> str:
    """
    :type path: Optional[str]
    :rtype: str
    """
    base = "basecode/"

    if path:
        base = base + path

    return base_path (base)
