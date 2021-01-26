import logging
import uuid
from typing import List

from service.infrastructure.sqlalchemy_client import SQLAlchemyClient

from service.dtos.data_dto import DataDTO
from service.infrastructure.daos.data_dao import DataDAO
from service.infrastructure.data_repository_interface import DataRepositoryInterface
from service.infrastructure.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyDataRepository(DataRepositoryInterface):
    def __init__(self: object, sqlalchemy_client: SQLAlchemyClient):
        logging.debug("SQLAlchemyDataRepository()")
        self.db_session = sqlalchemy_client.session
        self._crud_repository = SQLAlchemyCRUDRepository(
            sqlalchemy_client=sqlalchemy_client,
            dao_class=DataDAO,
        )

    def add_data(self: object, data_dto: DataDTO) -> None:
        logging.debug(
            f"SQLAlchemyDataRepository.add_data(data_dto={data_dto})"
        )
        self._crud_repository.add(dto=data_dto)

    def find_data(self: object) -> List[DataDTO]:
        logging.debug("SQLAlchemyDataRepository.find_data()")
        return self._crud_repository.find()

    def find_data_by_id(self: object, data_id: uuid.UUID) -> DataDTO:
        logging.debug(
            "SQLAlchemyDataRepository.find_data_by_id("
            f"data_id={data_id})"
        )
        return self._crud_repository.find_by_id(dto_id=data_id)

    def update_data(self: object, data_dto: DataDTO) -> None:
        logging.debug(
            "SQLAlchemyDataRepository.update_data("
            f"data_dto={data_dto})"
        )
        self._crud_repository.update(dto=data_dto)

    def reset(self: object) -> None:
        logging.debug("SQLAlchemyDataRepository.reset()")
        self._crud_repository.reset()

    def delete_data_by_id(self: object, data_id: uuid.UUID) -> None:
        logging.debug(
            f"SQLAlchemyDataRepository.delete_data(data_id={data_id})"
        )
        self._crud_repository.delete_by_id(dto_id=data_id)
