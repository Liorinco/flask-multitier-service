import uuid


def test_character_dto_instance(character_dict):
    from service.dtos.character_dto import CharacterDTO
    dto = CharacterDTO().from_dict(character_dict)
    assert isinstance(dto, CharacterDTO)
    assert isinstance(dto.id, uuid.UUID)
    assert isinstance(dto.name, str)
    assert isinstance(dto.age, int)
    assert isinstance(dto.weight, float)
    assert isinstance(dto.is_human, bool)
    assert isinstance(dto.hat_id, uuid.UUID) or dto.hat_id is None
    assert {
        "id": dto.id,
        "name": dto.name,
        "age": dto.age,
        "weight": dto.weight,
        "is_human": dto.is_human,
        "hat_id": dto.hat_id,
    } == character_dict


def test_character_dto_asdict(character_dict):
    from service.dtos.character_dto import CharacterDTO
    dto = CharacterDTO().from_dict(character_dict)
    assert dto.asdict() == character_dict


def test_character_dto_as_serialized_dict(character_dict):
    from service.dtos.character_dto import CharacterDTO
    dto = CharacterDTO().from_dict(character_dict)
    expected_result = character_dict.copy()
    expected_result["id"] = str(expected_result["id"])
    assert dto.as_serialized_dict() == expected_result
