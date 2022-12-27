from ....database.Contracts.IMigration import IMigration
from ....database import migrations
from typer import Typer, echo, progressbar
from rich.console import Console

application = Typer ()

name = "migration:up"
description = "Run migration to up"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    for migration in migrations:
        if isinstance (migration, IMigration):
            migration.up ()
