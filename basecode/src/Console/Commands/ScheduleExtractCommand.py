from typing import Union, List
from ...Extraction.Api.Contracts.IApi import IApi
from ...Extraction.Api import schedules as extractionsApi
from ...Extraction.Web import schedules as extractionsWeb
from .Concerns.ApiExtraction import ApiExtraction
from .Concerns.WebExtraction import WebExtraction
from datetime import timedelta
from asyncio import run, get_running_loop, sleep
from scheduler.asyncio import Scheduler
from typer import Typer, echo, progressbar
from rich.console import Console

class ScheduleCommand:

    async def __call__ (self) -> None:
        """
        :rtype: None
        :raises KeyboardInterrupt:
        """
        schedule = Scheduler (loop = get_running_loop ())
        extractions = [*extractionsApi, *extractionsWeb]

        for extraction in extractions:

            if isinstance (extraction, List) and len (extraction) == 2:
                period = extraction[0]
                job = extraction[1]

                if isinstance (period, timedelta) and (isinstance (job, IApi) or isinstance (job, str)):

                    schedule.cyclic (period, self.schedule, args = (job,))

        while True:
            try:
                await sleep (1)
            except KeyboardInterrupt:
                break

    async def schedule (self, job: Union[IApi, str]) -> None:
        """
        :type job: Union[IApi, str]
        :rtype: None
        """
        if isinstance (job, IApi):
            ApiExtraction () (job)
        elif isinstance (job, str):
            WebExtraction () (job)

application = Typer ()

name = "schedule:extract"
description = "Run the schedule of extraction"

@application.command (name = name, help = description)
def __call__ () -> None:
    """
    :rtype: None
    """
    run (ScheduleCommand () ())
