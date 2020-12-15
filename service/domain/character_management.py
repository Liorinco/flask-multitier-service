import logging
import uuid
from typing import List

from service.domain.character_management_interface import CharacterManagementInterface
from service.dtos.character_dto import CharacterDTO
from service.infrastructure.character_repository_interface import (
    CharacterRepositoryInterface
)


class CharacterManagement(CharacterManagementInterface):
    def __init__(self: object, repository: CharacterRepositoryInterface):
        logging.debug("CharacterManagement.__init__")
        self.__repository = repository

    def register_character(
        self: object,
        character_name: str,
        character_age: int,
        character_weight: float,
        character_is_human: bool,
    ) -> uuid.UUID:
        logging.debug("CharacterManagement.register_character")
        character_id = uuid.uuid4()
        character_dto = CharacterDTO().from_dict({
            "id": character_id,
            "name": character_name,
            "age": character_age,
            "weight": character_weight,
            "is_human": character_is_human,
        })
        self.__repository.add_character(character_dto=character_dto)
        return character_id

    def find_characters(self: object) -> List[CharacterDTO]:
        logging.debug("CharacterManagement.find_characters")
        return self.__repository.find_characters()

    def find_character_by_id(self: object, character_id: uuid.UUID) -> CharacterDTO:
        logging.debug("CharacterManagement.find_character_by_id")
        return self.__repository.find_character_by_id(character_id=character_id)

    def update_character(self: object, character_dto: CharacterDTO) -> None:
        logging.debug("CharacterManagement.update_character")
        self.__repository.update_character(character_dto=character_dto)

    def remove_character(self: object, character_id: uuid.UUID) -> None:
        logging.debug("CharacterManagement.remove_character")
        self.__repository.delete_character_by_id(character_id=character_id)
