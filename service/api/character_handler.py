import http
import logging
import uuid

import pydantic
from flask import request, Response
from flask_restplus import Resource

from service.api import characters_models
from service.domain.character_management_interface import CharacterManagementInterface
from service.dtos.character_dto import CharacterDTO
from service.exceptions import Conflict


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
        try:
            input_data = characters_models.POSTCharactersInput(
                **request.get_json()
            )
        except pydantic.ValidationError as error:
            return Response(
                response=error.json(),
                status=http.HTTPStatus.UNPROCESSABLE_ENTITY,
                mimetype="application/json",
            )
        try:
            character_dto = CharacterDTO().from_dict(
                {
                    "id": character_id,
                    "name": input_data.character_name,
                    "age": input_data.character_age,
                    "weight": input_data.character_weight,
                    "is_human": input_data.character_is_human,
                    "hat_id": input_data.character_hat_id,
                }
            )
            self.__domain.update_character(character_dto=character_dto)
        except Conflict as e:
            return Response(
                response=str(e),
                status=http.HTTPStatus.CONFLICT,
            )

    def delete(self: object, character_id: uuid.UUID):
        logging.debug(f"CharacterHandler.delete(character_id={character_id})")
        self.__domain.remove_character(character_id=character_id)
