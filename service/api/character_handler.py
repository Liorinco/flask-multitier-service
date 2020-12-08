import logging
import uuid

from flask_restplus import Resource

from service.domain.character_management_interfaces import CharacterManagementInterface


class CharacterHandler(Resource):
    def __init__(self: object, *args, domain: CharacterManagementInterface, **kwargs):
        logging.debug("CharacterHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def get(self: object, character_id: uuid.UUID):
        logging.debug(f"CharacterHandler.get(character_id={character_id})")
        character_dto = self.__domain.find_character_by_id(character_id=character_id)
        return character_dto.as_serialized_dict()
