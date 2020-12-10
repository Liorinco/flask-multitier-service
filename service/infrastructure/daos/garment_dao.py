from sqlalchemy import Column, Enum
from sqlalchemy.dialects.postgresql import UUID

from service.dtos.color import Color
from service.dtos.garment_dto import GarmentDTO
from service.infrastructure.daos.dao_base import DAOBase


class GarmentDAO(DAOBase):
    __tablename__ = "clothes"

    id = Column(UUID(as_uuid=True), primary_key=True)
    color = Column(
        Enum(Color, name="color", values_callable=lambda obj: [e.value for e in obj])
    )

    @classmethod
    def from_dto(cls: object, garment_dto: GarmentDTO) -> object:
        return cls(id=garment_dto.id, color=garment_dto.color)

    def asdict(self: object) -> dict:
        return {"id": self.id, "color": self.color}

    def to_dto(self: object) -> GarmentDTO:
        return GarmentDTO().from_dict(self.asdict())
