import uuid


def test_character_dto_instance():
    from service.dtos.character_dto import CharacterDTO
    dto_dict = {
        "id": uuid.uuid4(),
        "name": "dummy_name",
        "age": 33,
        "weight": 70.,
        "is_human": True,
    }
    dto = CharacterDTO().from_dict(dto_dict)
    assert isinstance(dto, CharacterDTO)
    assert isinstance(dto.id, uuid.UUID)
    assert isinstance(dto.name, str)
    assert isinstance(dto.age, int)
    assert isinstance(dto.weight, float)
    assert isinstance(dto.is_human, bool)
    assert {
        "id": dto.id,
        "name": dto.name,
        "age": dto.age,
        "weight": dto.weight,
        "is_human": dto.is_human,
    } == dto_dict


def test_character_dto_as_serialized_dict():
    from service.dtos.character_dto import CharacterDTO
    dto_dict = {
        "id": uuid.uuid4(),
        "name": "dummy_name",
        "age": 33,
        "weight": 70.,
        "is_human": True,
    }
    dto = CharacterDTO().from_dict(dto_dict)
    expected_result = {
        "id": str(dto_dict["id"]),
        "name": "dummy_name",
        "age": 33,
        "weight": 70.,
        "is_human": True,
    }
    assert dto.as_serialized_dict() == expected_result
