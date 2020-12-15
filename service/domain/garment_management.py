import logging
import uuid
from typing import List

from service.domain.garment_management_interface import GarmentManagementInterface
from service.dtos.color import Color
from service.dtos.garment_dto import GarmentDTO, GarmentArticle
from service.infrastructure.garment_repository_interface import GarmentRepositoryInterface


class GarmentManagement(GarmentManagementInterface):
    def __init__(self: object, repository: GarmentRepositoryInterface):
        logging.debug("GarmentManagement.__init__")
        self.__repository = repository

    def register_garment(
        self: object, garment_article: GarmentArticle, garment_color: Color,
    ) -> uuid.UUID:
        logging.debug("GarmentManagement.register_garment")
        garment_id = uuid.uuid4()
        garment_dto = GarmentDTO().from_dict({
            "id": garment_id, "article": garment_article, "color": garment_color,
        })
        self.__repository.add_garment(garment_dto=garment_dto)
        return garment_id

    def find_clothes(self: object) -> List[GarmentDTO]:
        logging.debug("GarmentManagement.find_clothes")
        return self.__repository.find_clothes()

    def find_garment_by_id(self: object, garment_id: uuid.UUID) -> GarmentDTO:
        logging.debug("GarmentManagement.find_garment_by_id")
        return self.__repository.find_garment_by_id(garment_id=garment_id)

    def update_garment(self: object, garment_dto: GarmentDTO) -> None:
        logging.debug("GarmentManagement.update_garment")
        self.__repository.update_garment(garment_dto=garment_dto)

    def remove_garment(self: object, garment_id: uuid.UUID) -> None:
        logging.debug("GarmentManagement.remove_garment")
        self.__repository.delete_garment_by_id(garment_id=garment_id)
