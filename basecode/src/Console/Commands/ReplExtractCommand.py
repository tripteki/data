import os
from ...Helpers.ApplicationPath import application_path
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "repl:extract"
description = "Run the repl of extraction"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    process = None

    try:
        os.chdir (application_path ("src/Extraction"))

        process = os.system ("/usr/bin/env python3 -m scrapy shell")

    except KeyboardInterrupt:
        if process:
            exit ()
