import os
import logging
from dotenv import load_dotenv

load_dotenv ()



BOT_NAME = os.environ.get ("PYTHON_NAME", "data")

ROBOTSTXT_OBEY = True
REDIRECT_ENABLED = True

# ITEM_PIPELINES = { #
#    "Web.pipelines.Pipeline": 300 #
# } #

# SPIDER_MIDDLEWARES = { #
#    "Web.middlewares.Middleware": 543 #
# } #

# DOWNLOADER_MIDDLEWARES = { #
#    "Web.middlewares.DownloaderMiddleware": 543 #
# } #

# DEFAULT_REQUEST_HEADERS = "{}" #
# USER_AGENT = "DEFAULT" #



MAIL_HOST = os.environ.get ("MAIL_HOST", "smtp.mail.com")
MAIL_PORT = os.environ.get ("MAIL_PORT", "587")
MAIL_USER = os.environ.get ("MAIL_USER", "admin@mail.com")
MAIL_PASS = os.environ.get ("MAIL_PASSWORD", "password")
MAIL_FROM = os.environ.get ("MAIL_FROM_ADDRESS", "admin@mail.com")



NEWSPIDER_MODULE = "Web.Spiders"
SPIDER_MODULES = ["Web.Spiders"]

if os.environ.get ("PYTHON_ENV", "production") == "production":
    REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
    TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

    if "SPIDERJOBS_DIR" in os.environ:
        JOBDIR = os.environ.get ("SPIDERJOBS_DIR")

SCHEDULER_DEBUG = True
LOG_STDOUT = True if os.environ.get ("PYTHON_ENV", "production") == "production" else False
LOG_LEVEL = int (os.environ.get ("LOG_LEVEL", str (logging.DEBUG)))

if "SPIDER_LOGFILE" in os.environ:
    LOG_FILE = os.environ.get ("SPIDER_LOGFILE")

if "SPIDERFILES_DIR" in os.environ:
    FILES_STORE = os.environ.get ("SPIDERFILES_DIR")

if "SPIDERIMAGES_DIR" in os.environ:
    IMAGES_STORE = os.environ.get ("SPIDERIMAGES_DIR")
