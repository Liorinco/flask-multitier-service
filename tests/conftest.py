import uuid

import pytest

import config

config.configure()


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
