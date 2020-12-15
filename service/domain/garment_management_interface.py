import uuid
from abc import ABC, abstractmethod
from typing import List

from service.dtos.color import Color
from service.dtos.garment_dto import GarmentDTO, GarmentArticle


class GarmentManagementInterface(ABC):
    @abstractmethod
    def register_garment(
        self: object, garment_article: GarmentArticle, garment_color: Color,
    ) -> uuid.UUID:
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
    def remove_garment(self: object, garment_id: uuid.UUID) -> None:
        pass
