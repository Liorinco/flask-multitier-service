import logging
import os

from service.api.flask_application import FlaskApplication


SERVICE_HOST = os.environ["SERVICE_HOST"]
SERVICE_PORT = int(os.environ["SERVICE_PORT"])
SERVICE_DEBUG = os.environ["SERVICE_DEBUG"]
DATABASE_URI = os.environ["DATABASE_URI"]


def configure_application():
    logging.basicConfig(level=logging.DEBUG)
    return FlaskApplication(host=SERVICE_HOST, port=SERVICE_PORT, debug=SERVICE_DEBUG)
