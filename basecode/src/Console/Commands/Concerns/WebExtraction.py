import signal
import re
from ....Helpers.ApplicationPath import application_path
from subprocess import call

class WebExtraction:

    def __call__ (self, extraction: str) -> None:
        """
        :type extraction: str
        :rtype: None
        """
        process = None

        try:
            if isinstance (extraction, str):
                command = "crawl"

                if bool (re.search ("\.py$", extraction)):
                    command = "runspider"
                    extraction = application_path (f"src/Extraction/Web/Spiders/{extraction}")

            process = call (f"/usr/bin/env python3 -m scrapy {command} {extraction}", cwd = application_path ("src/Extraction"), start_new_session = True, shell = True)

        except KeyboardInterrupt:
            if process:
                process.send_signal (signal.SIGKILL)
