from ...Extraction.Api import extractions
from .Concerns.ApiExtraction import ApiExtraction
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "extract:api"
description = "Run the api extraction"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    for extraction in extractions:
        ApiExtraction () (extraction)
