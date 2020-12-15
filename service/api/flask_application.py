import logging

from flask import Flask
from flask_restplus import Api, Namespace

from service.api.application_interface import ApplicationInterface
from service.api.character_handler import CharacterHandler
from service.api.characters_handler import CharactersHandler
from service.api.garment_handler import GarmentHandler
from service.api.clothes_handler import ClothesHandler
from service.domain.character_management_interface import CharacterManagementInterface
from service.domain.garment_management_interface import GarmentManagementInterface


class FlaskApplication(ApplicationInterface):
    def __init__(
        self: object,
        host: str,
        port: int,
        character_domain: CharacterManagementInterface,
        garment_domain: GarmentManagementInterface,
        debug: bool = False,
    ) -> object:
        logging.debug("FlaskApplication.__init__")
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.host = host
        self.port = port
        self.debug = debug

        # Character namespace
        character_namespace = Namespace("character")
        character_namespace.add_resource(
            CharacterHandler, "", resource_class_kwargs={"domain": character_domain}
        )
        self.api.add_namespace(
            character_namespace, path="/characters/<uuid:character_id>"
        )
        # Characters namespace
        characters_namespace = Namespace("characters")
        characters_namespace.add_resource(
            CharactersHandler, "", resource_class_kwargs={"domain": character_domain}
        )
        self.api.add_namespace(characters_namespace, path="/characters")
        # Garment namespace
        garment_namespace = Namespace("garment")
        garment_namespace.add_resource(
            GarmentHandler, "", resource_class_kwargs={"domain": garment_domain}
        )
        self.api.add_namespace(
            garment_namespace, path="/clothes/<uuid:garment_id>"
        )
        # Clothes namespace
        clothes_namespace = Namespace("clothes")
        clothes_namespace.add_resource(
            ClothesHandler, "", resource_class_kwargs={"domain": garment_domain}
        )
        self.api.add_namespace(clothes_namespace, path="/clothes")

    def run(self) -> None:
        logging.debug("FlaskApplication.run")
        self.app.run(host=self.host, port=self.port, debug=self.debug)
