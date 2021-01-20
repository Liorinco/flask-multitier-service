from sqlalchemy import Boolean, Column, Integer, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from service.dtos.character_dto import CharacterDTO
from service.infrastructure.daos.dao_base import DAOBase
# from service.infrastructure.daos.garment_dao import GarmentDAO


class CharacterDAO(DAOBase):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    weight = Column(Float)
    is_human = Column(Boolean)
    hat_id = Column(UUID(as_uuid=True), ForeignKey("clothes.id", ondelete="CASCADE"))
    clothes = relationship("GarmentDAO", back_populates="characters")

    @classmethod
    def from_dto(cls: object, character_dto: CharacterDTO) -> object:
        return cls(
            id=character_dto.id,
            name=character_dto.name,
            age=character_dto.age,
            weight=character_dto.weight,
            is_human=character_dto.is_human,
            hat_id=character_dto.hat_id,
        )

    def asdict(self: object) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "is_human": self.is_human,
            "hat_id": self.hat_id,
        }

    def to_dto(self: object) -> CharacterDTO:
        return CharacterDTO().from_dict(self.asdict())
