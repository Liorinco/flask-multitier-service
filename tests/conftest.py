import uuid

import pytest

import config

config.configure()

from helpers import CharacterFactory, GarmentFactory


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
        "hat_id": None,
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
        "hat_id": None,
    })


@pytest.fixture(autouse=True)  # autouse to clean database after all tests
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
        "hat_id": None,
    })
    character_repository.add_character(character_dto=character_dto)
    return character_dto


@pytest.fixture
def persisted_human_with_hat_dto(character_repository, persisted_garment_dto):
    from service.dtos.character_dto import CharacterDTO
    character_dto = CharacterDTO().from_dict({
        "id": uuid.uuid4(),
        "name": "dummy_character_name",
        "age": 20,
        "weight": 59.8,
        "is_human": True,
        "hat_id": persisted_garment_dto.id,
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
            "hat_id": None,
        })
        character_repository.add_character(character_dto=character_dto)
        character_dto_population.append(character_dto)
    return character_dto_population


@pytest.fixture
def persisted_human_with_hat_dto_population(
    character_repository, persisted_garment_dto
):
    from service.dtos.character_dto import CharacterDTO
    character_dto_population = []
    for x in range(1, 6):
        character_dto = CharacterDTO().from_dict({
            "id": uuid.uuid4(),
            "name": "dummy_character_name" + str(x),
            "age": 20 + x,
            "weight": 59.8 + x,
            "is_human": True,
            "hat_id": persisted_garment_dto.id,
        })
        character_repository.add_character(character_dto=character_dto)
        character_dto_population.append(character_dto)
    return character_dto_population


@pytest.fixture
def garment_dict():
    from service.dtos.color import Color
    from service.dtos.garment_dto import GarmentArticle
    return {"id": uuid.uuid4(), "article": GarmentArticle.HAT, "color": Color.PURPLE}


@pytest.fixture
def garment_dto(garment_dict):
    from service.dtos.garment_dto import GarmentDTO
    return GarmentDTO().from_dict(garment_dict)


@pytest.fixture(autouse=True)  # autouse to clean database after all tests
def garment_repository(sqlalchemy_client):
    from service.infrastructure.sqlalchemy_garment_repository import (
        SQLAlchemyGarmentRepository
    )
    repository = SQLAlchemyGarmentRepository(sqlalchemy_client=sqlalchemy_client)

    yield repository

    repository.reset()


@pytest.fixture
def persisted_garment_dto(garment_repository, garment_dto):
    garment_repository.add_garment(garment_dto=garment_dto)
    return garment_dto


@pytest.fixture
def yellow_hat_dict():
    from service.dtos.color import Color
    from service.dtos.garment_dto import GarmentArticle
    return {"id": uuid.uuid4(), "article": GarmentArticle.HAT, "color": Color.YELLOW}


@pytest.fixture
def yellow_hat_dto(yellow_hat_dict):
    from service.dtos.garment_dto import GarmentDTO
    return GarmentDTO().from_dict(yellow_hat_dict)


@pytest.fixture
def persisted_yellow_hat_dto(garment_repository, yellow_hat_dto):
    garment_repository.add_garment(garment_dto=yellow_hat_dto)
    return yellow_hat_dto


@pytest.fixture
def persisted_garment_dto_population(garment_repository):
    from service.dtos.color import Color
    from service.dtos.garment_dto import GarmentDTO, GarmentArticle
    garment_dto_population = []
    for x in range(1, 6):
        garment_dto = GarmentDTO().from_dict({
            "id": uuid.uuid4(),
            "article": [article for article in GarmentArticle][x % len(GarmentArticle)],
            "color": [color for color in Color][x % len(Color)],
        })
        garment_repository.add_garment(garment_dto=garment_dto)
        garment_dto_population.append(garment_dto)
    return garment_dto_population


@pytest.fixture(params=[CharacterFactory, GarmentFactory])
def entity_factory(request):
    return request.param


@pytest.fixture(autouse=True)  # autouse to clean database after all tests
def reset_persisted_entities(sqlalchemy_client, entity_factory):
    yield
    entity_factory.reset_persisted_entities(sqlalchemy_client=sqlalchemy_client)


@pytest.fixture
def persisted_entity(sqlalchemy_client, entity_factory):
    return entity_factory.generate_persisted_dto(sqlalchemy_client=sqlalchemy_client)


@pytest.fixture
def application():
    from service.config import configure_application
    app = configure_application()
    return app.app


@pytest.fixture
def client(application):
    return application.test_client()
