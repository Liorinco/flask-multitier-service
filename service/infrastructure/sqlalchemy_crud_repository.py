import logging
import uuid
from typing import List

from service.infrastructure.sqlalchemy_client import SQLAlchemyClient

from service.dtos.base_dto import BaseDTO
from service.infrastructure.daos.dao_base import DAOBase


class SQLAlchemyCRUDRepository:
    def __init__(self: object, sqlalchemy_client: SQLAlchemyClient, dao_class: DAOBase):
        logging.debug("SQLAlchemyCRUDRepository()")
        self.db_session = sqlalchemy_client.session
        self.dao_class = dao_class

    def add(self: object, dto: BaseDTO) -> None:
        logging.debug(f"SQLAlchemyCRUDRepository.add(dto={dto})")
        self.db_session.add(self.dao_class.from_dto(dto))
        self.db_session.commit()

    def find(self: object) -> List[BaseDTO]:
        logging.debug("SQLAlchemyCRUDRepository.find()")
        daos = self.db_session.query(self.dao_class).order_by(self.dao_class.id)
        return [dao.to_dto() for dao in daos]

    def find_by_id(self: object, dto_id: uuid.UUID) -> BaseDTO:
        logging.debug(f"SQLAlchemyCRUDRepository.find_by_id(dto_id={dto_id})")
        dao = (
            self.db_session.query(self.dao_class)
            .filter(self.dao_class.id == str(dto_id))
            .one()
        )
        return dao.to_dto()

    def update(self: object, dto: BaseDTO) -> None:
        logging.debug(f"SQLAlchemyCRUDRepository.update(dto={dto})")
        dao = self.dao_class.from_dto(dto)
        (
            self.db_session.query(self.dao_class)
            .filter(self.dao_class.id == str(dto.id))
            .update(dao.asdict())
        )
        self.db_session.commit()

    def reset(self: object) -> None:
        logging.debug("SQLAlchemyCRUDRepository.reset()")
        self.db_session.query(self.dao_class).delete()
        self.db_session.commit()

    def delete_by_id(self: object, dto_id: uuid.UUID) -> None:
        logging.debug(f"SQLAlchemyCRUDRepository.delete(dto_id={dto_id})")
        (
            self.db_session.query(self.dao_class)
            .filter(self.dao_class.id == str(dto_id))
            .delete()
        )
        self.db_session.commit()
