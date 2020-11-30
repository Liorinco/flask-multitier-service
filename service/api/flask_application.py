import logging

from flask import Flask
from flask_restplus import Api

from service.api.application_interface import ApplicationInterface


class FlaskApplication(ApplicationInterface):
    def __init__(self: object, host: str, port: int, debug: bool = False) -> object:
        logging.debug("FlaskApplication.__init__")
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.host = host
        self.port = port
        self.debug = debug

    def run(self) -> None:
        logging.debug("FlaskApplication.run")
        self.app.run(host=self.host, port=self.port, debug=self.debug)
