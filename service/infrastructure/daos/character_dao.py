from sqlalchemy import Boolean, Column, Integer, Float, String
from sqlalchemy.dialects.postgresql import UUID

from service.infrastructure.daos.dao_base import DAOBase


class CharacterDAO(DAOBase):
    __tablename__ = "characters"

    id = Column(UUID, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    weight = Column(Float)
    is_human = Column(Boolean)
