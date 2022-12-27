from ...Extraction.Web import extractions
from .Concerns.WebExtraction import WebExtraction
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "extract:web"
description = "Run the web extraction"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    for extraction in extractions:
        WebExtraction () (extraction)
