import os
import logging
from ..src.Helpers.LogNameSpace import log_name_space
from ..src.Helpers.ReportNameSpace import report_name_space

if "LOG_LEVEL" not in os.environ:
    os.environ["LOG_LEVEL"] = str (logging.DEBUG)

if "LOG_PATH" not in os.environ:
    os.environ["LOG_PATH"] = log_name_space ("/")

if "REPORT_PATH" not in os.environ:
    os.environ["REPORT_PATH"] = report_name_space ("/")
