import uuid
from abc import ABC, abstractmethod


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
