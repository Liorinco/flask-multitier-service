import uuid
from abc import ABC, abstractclassmethod

from service.dtos.character_dto import CharacterDTO
from service.dtos.color import Color
from service.dtos.garment_dto import GarmentDTO
from service.infrastructure.daos.character_dao import CharacterDAO
from service.infrastructure.daos.garment_dao import GarmentDAO


class Entity(ABC):
    @abstractclassmethod
    def generate_dict(cls):
        pass

    @classmethod
    def generate_dto(cls):
        return cls.dto_class().from_dict(cls.generate_dict())


class CharacterEntity(Entity):
    dto_class = CharacterDTO
    dao_class = CharacterDAO

    @classmethod
    def generate_dict(cls):
        return {
            "id": uuid.uuid4(),
            "name": "dumm_character_name",
            "age": 30,
            "weight": 70.3,
            "is_human": True,
        }


class GarmentEntity(Entity):
    dto_class = GarmentDTO
    dao_class = GarmentDAO

    @classmethod
    def generate_dict(cls):
        return {"id": uuid.uuid4(), "color": Color.YELLOW}
