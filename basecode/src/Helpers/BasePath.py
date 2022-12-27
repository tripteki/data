from typing import Optional
from os.path import abspath, dirname

def base_path (path: Optional[str] = None) -> str:
    """
    :type path: Optional[str]
    :rtype: str
    """
    base = "/../../../"

    if path:
        base = base + path

    return abspath (dirname (abspath (__file__)) + base)
