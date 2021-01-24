import uuid
from abc import ABC, abstractmethod
from typing import List

from service.dtos.character_dto import CharacterDTO


class CharacterRepositoryInterface(ABC):
    @abstractmethod
    def add_character(self: object, character_dto: CharacterDTO) -> None:
        pass

    @abstractmethod
    def find_characters(self: object) -> List[CharacterDTO]:
        pass

    @abstractmethod
    def find_character_by_id(self: object, character_id: uuid.UUID) -> CharacterDTO:
        pass

    @abstractmethod
    def find_characters_by_hat_id(self: object, hat_id: uuid.UUID) -> CharacterDTO:
        pass

    @abstractmethod
    def update_character(self: object, character_dto: CharacterDTO) -> None:
        pass

    @abstractmethod
    def delete_character_by_id(self: object, character_id: uuid.UUID) -> None:
        pass
