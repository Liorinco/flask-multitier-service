import logging
import uuid
from typing import List

from service.infrastructure.sqlalchemy_client import SQLAlchemyClient

from service.dtos.garment_dto import GarmentDTO
from service.infrastructure.garment_repository_interface import (
    GarmentRepositoryInterface
)
from service.infrastructure.daos.garment_dao import GarmentDAO
from service.infrastructure.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyGarmentRepository(GarmentRepositoryInterface):
    def __init__(self: object, sqlalchemy_client: SQLAlchemyClient):
        logging.debug("SQLAlchemyGarmentRepository()")
        self.db_session = sqlalchemy_client.session
        self._crud_repository = SQLAlchemyCRUDRepository(
            sqlalchemy_client=sqlalchemy_client, dao_class=GarmentDAO,
        )

    def add_garment(self: object, garment_dto: GarmentDTO) -> None:
        logging.debug(
            f"SQLAlchemyGarmentRepository.add_garment(garment_dto={garment_dto})"
        )
        self._crud_repository.add(dto=garment_dto)

    def find_clothes(self: object) -> List[GarmentDTO]:
        logging.debug("SQLAlchemyGarmentRepository.find_clothes()")
        return self._crud_repository.find()

    def find_garment_by_id(self: object, garment_id: uuid.UUID) -> GarmentDTO:
        logging.debug(
            "SQLAlchemyGarmentRepository.find_garment_by_id("
            f"garment_id={garment_id})"
        )
        return self._crud_repository.find_by_id(dto_id=garment_id)

    def update_garment(self: object, garment_dto: GarmentDTO) -> None:
        logging.debug(
            "SQLAlchemyGarmentRepository.update_garment("
            f"garment_dto={garment_dto})"
        )
        self._crud_repository.update(dto=garment_dto)

    def reset(self: object) -> None:
        logging.debug("SQLAlchemyGarmentRepository.reset()")
        self._crud_repository.reset()

    def delete_garment_by_id(self: object, garment_id: uuid.UUID) -> None:
        logging.debug(
            f"SQLAlchemyGarmentRepository.delete_garment(garment_id={garment_id})"
        )
        self._crud_repository.delete_by_id(dto_id=garment_id)
