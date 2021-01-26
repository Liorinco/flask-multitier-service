from sqlalchemy import Column, Date, Float, func, String
from sqlalchemy.dialects.postgresql import UUID

from service.dtos.data_dto import DataDTO
from service.infrastructure.daos.dao_base import DAOBase


class DataDAO(DAOBase):
    __tablename__ = "data"

    id = Column(UUID(as_uuid=True), primary_key=True)
    created_date = Column(Date, server_default=func.now())
    name = Column(String(50))
    value = Column(Float)

    @classmethod
    def from_dto(cls: object, data_dto: DataDTO) -> object:
        return cls(
            id=data_dto.id,
            reated_date=data_dto.created_date,
            name=data_dto.name,
            value=data_dto.value
        )

    def asdict(self: object) -> dict:
        return {
            "id": self.id,
            "created_date": self.created_date,
            "name": self.name,
            "value": self.value
        }

    def to_dto(self: object) -> DataDTO:
        return DataDTO().from_dict(self.asdict())
