import logging
import uuid
from typing import List

from service.infrastructure.sqlalchemy_client import SQLAlchemyClient

from service.dtos.character_dto import CharacterDTO
from service.infrastructure.character_repository_interface import (
    CharacterRepositoryInterface
)
from service.infrastructure.daos.character_dao import CharacterDAO
from service.infrastructure.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyCharacterRepository(CharacterRepositoryInterface):
    def __init__(self: object, sqlalchemy_client: SQLAlchemyClient):
        logging.debug("SQLAlchemyCharacterRepository()")
        self.db_session = sqlalchemy_client.session
        self._crud_repository = SQLAlchemyCRUDRepository(
            sqlalchemy_client=sqlalchemy_client,
            dao_class=CharacterDAO,
        )

    def add_character(self: object, character_dto: CharacterDTO) -> None:
        logging.debug(
            f"SQLAlchemyCharacterRepository.add_character(character_dto={character_dto})"
        )
        self._crud_repository.add(dto=character_dto)

    def find_characters(self: object) -> List[CharacterDTO]:
        logging.debug("SQLAlchemyCharacterRepository.find_characters()")
        return self._crud_repository.find()

    def find_character_by_id(self: object, character_id: uuid.UUID) -> CharacterDTO:
        logging.debug(
            "SQLAlchemyCharacterRepository.find_character_by_id("
            f"character_id={character_id})"
        )
        return self._crud_repository.find_by_id(dto_id=character_id)

    def update_character(self: object, character_dto: CharacterDTO) -> None:
        logging.debug(
            "SQLAlchemyCharacterRepository.update_character("
            f"character_dto={character_dto})"
        )
        self._crud_repository.update(dto=character_dto)

    def reset(self: object) -> None:
        logging.debug("SQLAlchemyCharacterRepository.reset()")
        self._crud_repository.reset()

    def delete_character_by_id(self: object, character_id: uuid.UUID) -> None:
        logging.debug(
            f"SQLAlchemyCharacterRepository.delete_character(character_id={character_id})"
        )
        self._crud_repository.delete_by_id(dto_id=character_id)
