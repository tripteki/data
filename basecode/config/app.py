import os

if "PYTHON_NAME" not in os.environ:
    os.environ["PYTHON_NAME"] = "Data Manipulation Command Line Tool"

if "PYTHON_ENV" not in os.environ:
    os.environ["PYTHON_ENV"] = "production"

if "TZ" not in os.environ:
    os.environ["TZ"] = "UTC"
