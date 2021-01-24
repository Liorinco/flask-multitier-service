import uuid

import pytest

from service.dtos.character_dto import CharacterDTO
from service.exceptions import Conflict, NotExpectedValueError


def test_character_dto_instance(character_dict):
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
    dto = CharacterDTO().from_dict(character_dict)
    assert dto.asdict() == character_dict


def test_character_dto_as_serialized_dict(character_dict):
    dto = CharacterDTO().from_dict(character_dict)
    expected_result = character_dict.copy()
    expected_result["id"] = str(expected_result["id"])
    assert dto.as_serialized_dict() == expected_result


def test_character_dto_non_human_cannot_wear_hat(character_dict):
    character_dict["is_human"] = False
    character_dict["hat_id"] = uuid.uuid4()
    with pytest.raises(Conflict) as e:
        CharacterDTO().from_dict(character_dict)
    assert str(e.value) == "Only humans can wear hats"


class TestCHaracterDTOYoungHumanTooBig:
    FAIL_AGE_LIMIT = 10
    FAIL_WEIGHT_LIMIT = 80.1

    def test_character_dto_young_human_too_big_fails(self, character_dict):
        character_dict["is_human"] = True
        character_dict["age"] = self.FAIL_AGE_LIMIT
        character_dict["weight"] = self.FAIL_WEIGHT_LIMIT
        with pytest.raises(Conflict) as e:
            CharacterDTO().from_dict(character_dict)
        assert str(e.value) == (
            f"Humans under or {self.FAIL_AGE_LIMIT} years old "
            f"cannot weigh more than {self.FAIL_WEIGHT_LIMIT - 0.1} kg"
        )

    def test_character_dto_young_human_too_big_age_limit(self, character_dict):
        character_dict["is_human"] = True
        character_dict["age"] = self.FAIL_AGE_LIMIT + 1
        character_dict["weight"] = self.FAIL_WEIGHT_LIMIT
        dto = CharacterDTO().from_dict(character_dict)
        assert dto.asdict() == character_dict

    def test_character_dto_young_human_too_big_weight_limit(self, character_dict):
        character_dict["is_human"] = True
        character_dict["age"] = self.FAIL_AGE_LIMIT
        character_dict["weight"] = self.FAIL_WEIGHT_LIMIT - 0.1
        dto = CharacterDTO().from_dict(character_dict)
        assert dto.asdict() == character_dict


def test_character_dto_age_cannot_be_negative(character_dict):
    age = -1
    character_dict["age"] = age
    with pytest.raises(NotExpectedValueError) as e:
        CharacterDTO().from_dict(character_dict)
    assert str(e.value) == (
        f"`age` expects `{type(age)}`, but `{type(age)}` is given (must be positive)"
    )
