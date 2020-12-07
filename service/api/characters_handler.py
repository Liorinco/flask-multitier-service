import logging

from flask import request
from flask_restplus import Resource

from service.domain.character_management_interfaces import CharacterManagementInterface


class CharactersHandler(Resource):
    def __init__(self: object, *args, domain: CharacterManagementInterface, **kwargs):
        logging.debug("CharactersHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def post(self: object):
        logging.debug("CharactersHandler.post")
        json_data = request.get_json()
        character_id = self.__domain.register_character(**json_data)
        return {"character_id": str(character_id)}
