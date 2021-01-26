import uuid
from abc import ABC, abstractclassmethod
from datetime import datetime

from service.dtos.base_dto import BaseDTO
from service.dtos.character_dto import CharacterDTO
from service.dtos.color import Color
from service.dtos.data_dto import DataDTO
from service.dtos.garment_dto import GarmentDTO, GarmentArticle
from service.infrastructure.daos.character_dao import CharacterDAO
from service.infrastructure.daos.data_dao import DataDAO
from service.infrastructure.daos.garment_dao import GarmentDAO
from service.infrastructure.sqlalchemy_character_repository import (
    SQLAlchemyCharacterRepository
)
from service.infrastructure.sqlalchemy_client import SQLAlchemyClient
from service.infrastructure.sqlalchemy_data_repository import SQLAlchemyDataRepository
from service.infrastructure.sqlalchemy_garment_repository import (
    SQLAlchemyGarmentRepository
)


class EntityFactory(ABC):
    @property
    @abstractclassmethod
    def dto_class(cls):
        pass

    @property
    @abstractclassmethod
    def dao_class(cls):
        pass

    @property
    @abstractclassmethod
    def repository_class(cls):
        pass

    @property
    @abstractclassmethod
    def repository_add_entity_method_name(cls):
        pass

    @property
    @abstractclassmethod
    def repository_find_entities_method_name(cls):
        pass

    @property
    @abstractclassmethod
    def repository_find_entity_by_id_method_name(cls):
        pass

    @property
    @abstractclassmethod
    def repository_update_entity_method_name(cls):
        pass

    @property
    @abstractclassmethod
    def repository_reset_entities_method_name(cls):
        pass

    @property
    @abstractclassmethod
    def repository_delete_entity_by_id_method_name(cls):
        pass

    @abstractclassmethod
    def generate_dict(cls):
        pass

    @classmethod
    def generate_dto(cls):
        return cls.dto_class().from_dict(cls.generate_dict())

    @classmethod
    def persist_dto(cls, sqlalchemy_client: SQLAlchemyClient, entity_dto: BaseDTO):
        repository = cls.repository_class(sqlalchemy_client=sqlalchemy_client)
        add_entity = getattr(repository, cls.repository_add_entity_method_name)
        add_entity(entity_dto)

    @classmethod
    def generate_persisted_dto(cls, sqlalchemy_client: SQLAlchemyClient):
        dto = cls.generate_dto()
        cls.persist_dto(sqlalchemy_client=sqlalchemy_client, entity_dto=dto)
        return dto

    @classmethod
    def find_persisted_dtos(cls, sqlalchemy_client: SQLAlchemyClient):
        repository = cls.repository_class(sqlalchemy_client=sqlalchemy_client)
        find_entities = getattr(repository, cls.repository_find_entities_method_name)
        return find_entities()

    @classmethod
    def reset_persisted_entities(cls, sqlalchemy_client: SQLAlchemyClient):
        repository = cls.repository_class(sqlalchemy_client=sqlalchemy_client)
        reset_entities = getattr(repository, cls.repository_reset_entities_method_name)
        reset_entities()

    @abstractclassmethod
    def generate_entity_update(cls, entity_dto: BaseDTO) -> BaseDTO:
        pass


class CharacterFactory(EntityFactory):
    dto_class = CharacterDTO
    dao_class = CharacterDAO
    repository_class = SQLAlchemyCharacterRepository
    repository_add_entity_method_name = "add_character"
    repository_find_entities_method_name = "find_characters"
    repository_find_entity_by_id_method_name = "find_character_by_id"
    repository_update_entity_method_name = "update_character"
    repository_reset_entities_method_name = "reset"
    repository_delete_entity_by_id_method_name = "delete_character_by_id"

    @classmethod
    def generate_dict(cls):
        return {
            "id": uuid.uuid4(),
            "name": "dumm_character_name",
            "age": 30,
            "weight": 70.3,
            "is_human": True,
            "hat_id": None,
        }

    @classmethod
    def generate_entity_update(cls, entity_dto: CharacterDTO) -> CharacterDTO:
        updated_dto = CharacterDTO()
        updated_dto.id = entity_dto.id
        updated_dto.name = "updated_" + entity_dto.name
        updated_dto.age = entity_dto.age + 3
        updated_dto.weight = entity_dto.weight + 8.6
        updated_dto.is_human = not entity_dto.is_human
        updated_dto.hat_id = None
        return updated_dto


class GarmentFactory(EntityFactory):
    dto_class = GarmentDTO
    dao_class = GarmentDAO
    repository_class = SQLAlchemyGarmentRepository
    repository_add_entity_method_name = "add_garment"
    repository_find_entities_method_name = "find_clothes"
    repository_find_entity_by_id_method_name = "find_garment_by_id"
    repository_update_entity_method_name = "update_garment"
    repository_reset_entities_method_name = "reset"
    repository_delete_entity_by_id_method_name = "delete_garment_by_id"

    @classmethod
    def generate_dict(cls):
        return {"id": uuid.uuid4(), "article": GarmentArticle.HAT, "color": Color.YELLOW}

    @classmethod
    def generate_entity_update(cls, entity_dto: GarmentDTO) -> GarmentDTO:
        updated_dto = GarmentDTO()
        updated_dto.id = entity_dto.id
        updated_dto.article = entity_dto.article
        colors = [color for color in Color if color != entity_dto.color]
        updated_dto.color = colors[0]
        return updated_dto


class DataFactory(EntityFactory):
    dto_class = DataDTO
    dao_class = DataDAO
    repository_class = SQLAlchemyDataRepository
    repository_add_entity_method_name = "add_data"
    repository_find_entities_method_name = "find_data"
    repository_find_entity_by_id_method_name = "find_data_by_id"
    repository_update_entity_method_name = "update_data"
    repository_reset_entities_method_name = "reset"
    repository_delete_entity_by_id_method_name = "delete_data_by_id"

    @classmethod
    def generate_dict(cls):
        return {
            "id": uuid.uuid4(),
            "created_date": datetime.now(),
            "name": "dumm_data_name",
            "value": 70.3,
        }

    @classmethod
    def generate_entity_update(cls, entity_dto: DataDTO) -> DataDTO:
        updated_dto = DataDTO()
        updated_dto.id = entity_dto.id
        updated_dto.created_date = datetime.now()
        updated_dto.name = "updated_" + entity_dto.name
        updated_dto.value = entity_dto.value + 8.6
        return updated_dto
