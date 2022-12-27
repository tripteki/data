import os
from ..src.Helpers.LogNameSpace import log_name_space
from ..src.Helpers.ReportNameSpace import report_name_space

if os.environ.get ("PYTHON_ENV", "production") == "production":

    if "SPIDER_LOGFILE" not in os.environ:
        os.environ["SPIDER_LOGFILE"] = "spider.log"

    if "SPIDER_HTML" not in os.environ:
        os.environ["SPIDER_HTML"] = "spider.html"

if os.environ.get ("PYTHON_ENV", "production") != "production":

    if "SPIDERJOBS_DIR" not in os.environ:
        os.environ["SPIDERJOBS_DIR"] = log_name_space ("/") + "/spider/jobs"

    if "SPIDERFILES_DIR" not in os.environ:
        os.environ["SPIDERFILES_DIR"] = report_name_space ("/") + "/spider/files"

    if "SPIDERIMAGES_DIR" not in os.environ:
        os.environ["SPIDERIMAGES_DIR"] = report_name_space ("/") + "/spider/images"
