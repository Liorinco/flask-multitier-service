import logging
import uuid

from flask import request
from flask_restplus import Resource

from service.domain.character_management_interface import CharacterManagementInterface
from service.dtos.character_dto import CharacterDTO


class CharacterHandler(Resource):
    def __init__(self: object, *args, domain: CharacterManagementInterface, **kwargs):
        logging.debug("CharacterHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def get(self: object, character_id: uuid.UUID):
        logging.debug(f"CharacterHandler.get(character_id={character_id})")
        character_dto = self.__domain.find_character_by_id(character_id=character_id)
        return character_dto.as_serialized_dict()

    def put(self: object, character_id: uuid.UUID):
        logging.debug(f"CharacterHandler.put(character_id={character_id})")
        character_data = {"id": character_id}
        character_data.update(request.get_json())
        character_dto = CharacterDTO().from_dict(character_data)
        self.__domain.update_character(character_dto=character_dto)

    def delete(self: object, character_id: uuid.UUID):
        logging.debug(f"CharacterHandler.delete(character_id={character_id})")
        self.__domain.remove_character(character_id=character_id)
