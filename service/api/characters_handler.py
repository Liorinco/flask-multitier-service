import http
import logging

import pydantic
from flask import request, Response
from flask_restplus import Resource

from service.api import characters_models
from service.domain.character_management_interface import CharacterManagementInterface
from service.exceptions import Conflict


class CharactersHandler(Resource):
    def __init__(self: object, *args, domain: CharacterManagementInterface, **kwargs):
        logging.debug("CharactersHandler.__init__")
        self.__domain = domain
        super().__init__(*args, **kwargs)

    def post(self: object):
        logging.debug("CharactersHandler.post")
        try:
            input_data = characters_models.POSTCharactersInput(
                **request.get_json()
            ).dict()
        except pydantic.ValidationError as e:
            return Response(
                response=e.json(),
                status=http.HTTPStatus.UNPROCESSABLE_ENTITY,
                mimetype="application/json",
            )
        try:
            character_id = self.__domain.register_character(**input_data)
        except Conflict as e:
            return Response(
                response=str(e),
                status=http.HTTPStatus.CONFLICT,
            )
        return {"character_id": str(character_id)}

    def get(self: object):
        logging.debug("CharactersHandler.get")
        character_dtos = self.__domain.find_characters()
        return {
            "characters": [
                character_dto.as_serialized_dict() for character_dto in character_dtos
            ]
        }
