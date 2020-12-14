import uuid
from abc import ABC, abstractmethod
from typing import List

from service.dtos.garment_dto import GarmentDTO


class GarmentRepositoryInterface(ABC):
    @abstractmethod
    def add_garment(self: object, garment_dto: GarmentDTO) -> None:
        pass

    @abstractmethod
    def find_clothes(self: object) -> List[GarmentDTO]:
        pass

    @abstractmethod
    def find_garment_by_id(self: object, garment_id: uuid.UUID) -> GarmentDTO:
        pass

    @abstractmethod
    def update_garment(self: object, garment_dto: GarmentDTO) -> None:
        pass

    @abstractmethod
    def delete_garment_by_id(self: object, garment_id: uuid.UUID) -> None:
        pass
