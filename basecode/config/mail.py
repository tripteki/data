import os

if "MAIL_HOST" not in os.environ:
    os.environ["MAIL_HOST"] = "smtp.mail.com"

if "MAIL_PORT" not in os.environ:
    os.environ["MAIL_PORT"] = "587"

if "MAIL_USER" not in os.environ:
    os.environ["MAIL_USER"] = "admin@mail.com"

if "MAIL_PASSWORD" not in os.environ:
    os.environ["MAIL_PASSWORD"] = "password"

if "MAIL_FROM_ADDRESS" not in os.environ:
    os.environ["MAIL_FROM_ADDRESS"] = "admin@mail.com"
