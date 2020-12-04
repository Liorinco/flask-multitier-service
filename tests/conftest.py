import uuid

import pytest

import config

config.configure()


@pytest.fixture(scope="session")
def sqlalchemy_client():
    from service.infrastructure.sqlalchemy_client import SQLAlchemyClient
    return SQLAlchemyClient(database_uri=config.DATABASE_URI)


@pytest.fixture
def character_dict():
    return {
        "id": uuid.uuid4(),
        "name": "dumm_character_name",
        "age": 30,
        "weight": 70.3,
        "is_human": True,
    }


@pytest.fixture
def character_dto():
    from service.dtos.character_dto import CharacterDTO
    return CharacterDTO().from_dict({
        "id": uuid.uuid4(),
        "name": "dummy_character_name",
        "age": 33,
        "weight": 70.,
        "is_human": True,
    })


@pytest.fixture
def character_repository(sqlalchemy_client):
    from service.infrastructure.sqlalchemy_character_repository import (
        SQLAlchemyCharacterRepository
    )
    repository = SQLAlchemyCharacterRepository(sqlalchemy_client=sqlalchemy_client)

    yield repository

    repository.reset()


@pytest.fixture
def persisted_character_dto(character_repository):
    from service.dtos.character_dto import CharacterDTO
    character_dto = CharacterDTO().from_dict({
        "id": uuid.uuid4(),
        "name": "dummy_character_name",
        "age": 20,
        "weight": 59.8,
        "is_human": False,
    })
    character_repository.add_character(character_dto=character_dto)
    return character_dto


@pytest.fixture
def persisted_character_dto_population(character_repository):
    from service.dtos.character_dto import CharacterDTO
    character_dto_population = []
    for x in range(1, 6):
        character_dto = CharacterDTO().from_dict({
            "id": uuid.uuid4(),
            "name": "dummy_character_name" + str(x),
            "age": 20 + x,
            "weight": 59.8 + x,
            "is_human": True,
        })
        character_repository.add_character(character_dto=character_dto)
        character_dto_population.append(character_dto)
    return character_dto_population
