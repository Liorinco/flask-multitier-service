from sqlalchemy import Boolean, Column, Integer, Float, String
from sqlalchemy.dialects.postgresql import UUID

from service.dtos.character_dto import CharacterDTO
from service.infrastructure.daos.dao_base import DAOBase


class CharacterDAO(DAOBase):
    __tablename__ = "characters"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    weight = Column(Float)
    is_human = Column(Boolean)

    @classmethod
    def from_dto(cls: object, character_dto: CharacterDTO) -> object:
        return cls(
            id=character_dto.id,
            name=character_dto.name,
            age=character_dto.age,
            weight=character_dto.weight,
            is_human=character_dto.is_human,
        )

    def asdict(self: object) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "is_human": self.is_human,
        }

    def to_dto(self: object) -> CharacterDTO:
        return CharacterDTO().from_dict(self.asdict())
