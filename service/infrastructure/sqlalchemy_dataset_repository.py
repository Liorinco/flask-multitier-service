import logging
import uuid
from typing import List

from service.infrastructure.sqlalchemy_client import SQLAlchemyClient

from service.dtos.dataset_dto import DataSetDTO
from service.infrastructure.daos.dataset_dao import DataSetDAO
from service.infrastructure.dataset_repository_interface import DataSetRepositoryInterface
from service.infrastructure.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository


class SQLAlchemyDataSetRepository(DataSetRepositoryInterface):
    def __init__(self: object, sqlalchemy_client: SQLAlchemyClient):
        logging.debug("SQLAlchemyDataSetRepository()")
        self.db_session = sqlalchemy_client.session
        self._crud_repository = SQLAlchemyCRUDRepository(
            sqlalchemy_client=sqlalchemy_client,
            dao_class=DataSetDAO,
        )

    def add_dataset(self: object, dataset_dto: DataSetDTO) -> None:
        logging.debug(
            f"SQLAlchemyDataSetRepository.add_dataset(dataset_dto={dataset_dto})"
        )
        self._crud_repository.add(dto=dataset_dto)

    def find_dataset(self: object) -> List[DataSetDTO]:
        logging.debug("SQLAlchemyDataSetRepository.find_dataset()")
        return self._crud_repository.find()

    def find_dataset_by_id(self: object, dataset_id: uuid.UUID) -> DataSetDTO:
        logging.debug(
            "SQLAlchemyDataSetRepository.find_dataset_by_id("
            f"dataset_id={dataset_id})"
        )
        return self._crud_repository.find_by_id(dto_id=dataset_id)

    def update_dataset(self: object, dataset_dto: DataSetDTO) -> None:
        logging.debug(
            "SQLAlchemyDataSetRepository.update_dataset("
            f"dataset_dto={dataset_dto})"
        )
        self._crud_repository.update(dto=dataset_dto)

    def reset(self: object) -> None:
        logging.debug("SQLAlchemyDataSetRepository.reset()")
        self.db_session.query("datasets_data").delete()
        self.db_session.commit()
        self._crud_repository.reset()

    def delete_dataset_by_id(self: object, dataset_id: uuid.UUID) -> None:
        logging.debug(
            f"SQLAlchemyDataSetRepository.delete_dataset(dataset_id={dataset_id})"
        )
        self._crud_repository.delete_by_id(dto_id=dataset_id)
