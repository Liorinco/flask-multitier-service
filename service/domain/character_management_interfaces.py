import uuid
from abc import ABC, abstractmethod
from typing import List

from service.dtos.character_dto import CharacterDTO


class CharacterManagementInterface(ABC):
    @abstractmethod
    def register_character(
        self: object,
        character_name: str,
        character_age: int,
        character_weight: float,
        character_is_human: bool,
    ) -> uuid.UUID:
        pass

    @abstractmethod
    def find_characters(self: object) -> List[CharacterDTO]:
        pass

    @abstractmethod
    def find_character_by_id(self: object, character_id: uuid.UUID) -> CharacterDTO:
        pass

    @abstractmethod
    def update_character(self: object, character_dto: CharacterDTO) -> None:
        pass
