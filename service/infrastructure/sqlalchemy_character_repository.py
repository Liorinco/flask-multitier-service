import logging
import uuid
from typing import List

from service.infrastructure.sqlalchemy_client import Session

from service.dtos.character_dto import CharacterDTO
from service.infrastructure.character_repository_interface import (
    CharacterRepositoryInterface
)
from service.infrastructure.daos.character_dao import CharacterDAO


class SQLAlchemyCharacterRepository(CharacterRepositoryInterface):
    def __init__(self: object):
        logging.debug("SQLAlchemyCharacterRepository()")
        self.session = Session()

    def add_character(self: object, character_dto: CharacterDTO) -> None:
        logging.debug(
            f"SQLAlchemyCharacterRepository.add_character(character_dto={character_dto})"
        )
        self.session.add(CharacterDAO.from_dto(character_dto=character_dto))
        self.session.commit()

    def find_characters(self: object) -> List[CharacterDTO]:
        logging.debug("SQLAlchemyCharacterRepository.find_characters()")
        characters_dao = self.session.query(CharacterDAO).order_by(CharacterDAO.id)
        return [character_dao.to_dto() for character_dao in characters_dao]

    def find_character_by_id(self: object, character_id: uuid.UUID) -> CharacterDTO:
        logging.debug(
            "SQLAlchemyCharacterRepository.find_character_by_id("
            f"character_id={character_id})"
        )
        character_dao = (
            self.session.query(CharacterDAO)
            .filter(CharacterDAO.id == str(character_id))
            .one()
        )
        return character_dao.to_dto()

    def update_character(self: object, character_dto: CharacterDTO) -> None:
        logging.debug(
            "SQLAlchemyCharacterRepository.update_character("
            f"character_dto={character_dto})"
        )
        character_dao = CharacterDAO.from_dto(character_dto=character_dto)
        (
            self.session.query(CharacterDAO)
            .filter(CharacterDAO.id == str(character_dto.id))
            .update(character_dao.asdict())
        )
        self.session.commit()

    def reset(self: object) -> None:
        logging.debug("SQLAlchemyCharacterRepository.reset()")
        self.session.query(CharacterDAO).delete()
        self.session.commit()

    def delete_character_by_id(self: object, character_id: uuid.UUID) -> None:
        logging.debug(
            f"SQLAlchemyCharacterRepository.delete_character(character_id={character_id})"
        )
        (
            self.session.query(CharacterDAO)
            .filter(CharacterDAO.id == str(character_id))
            .delete()
        )
        self.session.commit()
