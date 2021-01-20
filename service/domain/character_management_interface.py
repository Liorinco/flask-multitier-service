import uuid
from abc import ABC, abstractmethod
from typing import List, Optional

from service.dtos.character_dto import CharacterDTO


class CharacterManagementInterface(ABC):
    @abstractmethod
    def register_character(
        self: object,
        character_name: str,
        character_age: int,
        character_weight: float,
        character_is_human: bool,
        character_hat_id: Optional[uuid.UUID],
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

    @abstractmethod
    def remove_character(self: object, character_id: uuid.UUID) -> None:
        pass
