import logging
import uuid

from flask import request
from flask_restplus import Resource

from service.domain.character_management_interface import CharacterManagementInterface


class CharactersHandler(Resource):
    def __init__(self: object, *args, domain: CharacterManagementInterface, **kwargs):
        logging.debug("CharactersHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def post(self: object):
        logging.debug("CharactersHandler.post")
        json_data = request.get_json()
        json_data["character_hat_id"] = (
            None
            if json_data["character_hat_id"] is None
            else uuid.UUID(json_data["character_hat_id"])
        )
        character_id = self.__domain.register_character(**json_data)
        return {"character_id": str(character_id)}

    def get(self: object):
        logging.debug("CharactersHandler.get")
        character_dtos = self.__domain.find_characters()
        return {
            "characters": [
                character_dto.as_serialized_dict() for character_dto in character_dtos
            ]
        }
