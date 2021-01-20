from sqlalchemy import Column, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from service.dtos.color import Color
from service.dtos.garment_dto import GarmentDTO, GarmentArticle
from service.infrastructure.daos.dao_base import DAOBase
# from service.infrastructure.daos.character_dao import CharacterDAO


class GarmentDAO(DAOBase):
    __tablename__ = "clothes"

    id = Column(UUID(as_uuid=True), primary_key=True)
    article = Column(
        Enum(
            GarmentArticle,
            name="article",
            values_callable=lambda obj: [e.value for e in obj]
        )
    )
    color = Column(
        Enum(Color, name="color", values_callable=lambda obj: [e.value for e in obj])
    )
    characters = relationship("CharacterDAO", back_populates="clothes", uselist=False)

    @classmethod
    def from_dto(cls: object, garment_dto: GarmentDTO) -> object:
        return cls(
            id=garment_dto.id, article=garment_dto.article, color=garment_dto.color
        )

    def asdict(self: object) -> dict:
        return {"id": self.id, "article": self.article, "color": self.color}

    def to_dto(self: object) -> GarmentDTO:
        return GarmentDTO().from_dict(self.asdict())
