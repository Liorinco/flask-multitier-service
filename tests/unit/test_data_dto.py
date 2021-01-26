import uuid

from datetime import datetime

from service.dtos.data_dto import DataDTO


def test_data_dto_instance(data_dict):
    dto = DataDTO().from_dict(data_dict)
    assert isinstance(dto, DataDTO)
    assert isinstance(dto.id, uuid.UUID)
    assert isinstance(dto.created_date, datetime)
    assert isinstance(dto.name, str)
    assert isinstance(dto.value, float)
    assert {
        "id": dto.id,
        "created_date": dto.created_date,
        "name": dto.name,
        "value": dto.value,
    } == data_dict


def test_data_dto_asdict(data_dict):
    dto = DataDTO().from_dict(data_dict)
    assert dto.asdict() == data_dict


def test_data_dto_as_serialized_dict(data_dict):
    dto = DataDTO().from_dict(data_dict)
    expected_result = data_dict.copy()
    expected_result["id"] = str(expected_result["id"])
    expected_result["created_date"] = expected_result["created_date"].isoformat()
    assert dto.as_serialized_dict() == expected_result
