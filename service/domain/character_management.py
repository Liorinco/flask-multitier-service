import logging
import uuid
from typing import List, Optional

from service.domain.character_management_interface import CharacterManagementInterface
from service.dtos.character_dto import CharacterDTO
from service.dtos.color import Color
from service.dtos.garment_dto import GarmentDTO
from service.exceptions import Conflict
from service.infrastructure.character_repository_interface import (
    CharacterRepositoryInterface
)
from service.infrastructure.garment_repository_interface import GarmentRepositoryInterface


class CharacterManagement(CharacterManagementInterface):
    def __init__(
        self: object,
        repository: CharacterRepositoryInterface,
        garment_repository: GarmentRepositoryInterface
    ):
        logging.debug("CharacterManagement.__init__")
        self.__repository = repository
        self.__garment_repository = garment_repository  # TODO: should be removed to use application layer instead

    def register_character(
        self: object,
        character_name: str,
        character_age: int,
        character_weight: float,
        character_is_human: bool,
        character_hat_id: Optional[uuid.UUID],
    ) -> uuid.UUID:
        logging.debug("CharacterManagement.register_character")
        character_hat = (
            None
            if character_hat_id is None
            else self.__garment_repository.find_garment_by_id(garment_id=character_hat_id)
        )
        self._raise_conflict_if_not_valid_character(
            character_name=character_name,
            character_age=character_age,
            character_weight=character_weight,
            character_is_human=character_is_human,
            character_hat=character_hat,
        )
        character_id = uuid.uuid4()
        character_dto = CharacterDTO().from_dict({
            "id": character_id,
            "name": character_name,
            "age": character_age,
            "weight": character_weight,
            "is_human": character_is_human,
            "hat_id": character_hat_id,
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
        character_hat = (
            None
            if character_dto.hat_id is None
            else self.__garment_repository.find_garment_by_id(
                garment_id=character_dto.hat_id
            )
        )
        self._raise_conflict_if_not_valid_character(
            character_name=character_dto.name,
            character_age=character_dto.age,
            character_weight=character_dto.weight,
            character_is_human=character_dto.is_human,
            character_hat=character_hat,
        )
        self.__repository.update_character(character_dto=character_dto)

    def remove_character(self: object, character_id: uuid.UUID) -> None:
        logging.debug("CharacterManagement.remove_character")
        self.__repository.delete_character_by_id(character_id=character_id)

    def _raise_conflict_if_character_with_p_in_name_wears_yellow_hat(
        self, character_name: str, character_hat=GarmentDTO
    ) -> None:
        if "p" in character_name and character_hat.color is Color.YELLOW:
            raise Conflict(
                error_message=(
                    "Characters whose a 'p' is in there name cannot where a yellow hat"
                )
            )

    def _raise_conflict_if_not_valid_character(
        self: object,
        character_name: str,
        character_age: int,
        character_weight: float,
        character_is_human: bool,
        character_hat: GarmentDTO,
    ) -> None:
        self._raise_conflict_if_character_with_p_in_name_wears_yellow_hat(
            character_name=character_name, character_hat=character_hat
        )
