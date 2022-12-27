from .Version import Version
from .Console.Commands.VersionCommand import application as VersionCommand, name as VersionCommandName, description as VersionCommandDescription
from .Console.Commands.MigrationUpCommand import application as MigrationUpCommand, name as MigrationUpCommandName, description as MigrationUpCommandDescription
from .Console.Commands.MigrationDownCommand import application as MigrationDownCommand, name as MigrationDownCommandName, description as MigrationDownCommandDescription
from .Console.Commands.ExtractApiCommand import application as ExtractApiCommand, name as ExtractApiCommandName, description as ExtractApiCommandDescription
from .Console.Commands.ExtractWebCommand import application as ExtractWebCommand, name as ExtractWebCommandName, description as ExtractWebCommandDescription
from .Console.Commands.ReplExtractCommand import application as ReplExtractCommand, name as ReplExtractCommandName, description as ReplExtractCommandDescription
from .Console.Commands.ScheduleExtractCommand import application as ScheduleExtractCommand, name as ScheduleExtractCommandName, description as ScheduleExtractCommandDescription
from dotenv import load_dotenv
from os import environ
from typer import Typer

load_dotenv ()
from ..config import app
from ..config import logging
from ..config import spider
from ..config import database
from ..config import mail
from ..config import thirdparty

application = Typer (help = environ["PYTHON_NAME"])

application.add_typer (VersionCommand, name = VersionCommandName, help = VersionCommandDescription)
application.add_typer (MigrationUpCommand, name = MigrationUpCommandName, help = MigrationUpCommandDescription)
application.add_typer (MigrationDownCommand, name = MigrationDownCommandName, help = MigrationDownCommandDescription)
application.add_typer (ExtractApiCommand, name = ExtractApiCommandName, help = ExtractApiCommandDescription)
application.add_typer (ExtractWebCommand, name = ExtractWebCommandName, help = ExtractWebCommandDescription)
application.add_typer (ReplExtractCommand, name = ReplExtractCommandName, help = ReplExtractCommandDescription)
application.add_typer (ScheduleExtractCommand, name = ScheduleExtractCommandName, help = ScheduleExtractCommandDescription)

if __name__ == "__main__":

    application ()
