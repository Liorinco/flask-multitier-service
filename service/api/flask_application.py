import logging

from flask import Flask
from flask_restplus import Api, Namespace

from service.api.application_interface import ApplicationInterface
from service.api.characters_handler import CharactersHandler
from service.domain.character_management_interfaces import CharacterManagementInterface


class FlaskApplication(ApplicationInterface):
    def __init__(
        self: object,
        host: str,
        port: int,
        character_domain: CharacterManagementInterface,
        debug: bool = False,
    ) -> object:
        logging.debug("FlaskApplication.__init__")
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.host = host
        self.port = port
        self.debug = debug

        # Characters namespace
        characters_namespace = Namespace("characters")
        characters_namespace.add_resource(
            CharactersHandler, "", resource_class_kwargs={"domain": character_domain}
        )
        self.api.add_namespace(characters_namespace, path="/characters")

    def run(self) -> None:
        logging.debug("FlaskApplication.run")
        self.app.run(host=self.host, port=self.port, debug=self.debug)
