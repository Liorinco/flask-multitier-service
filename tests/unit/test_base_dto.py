import uuid


def test_base_dto_instance():
    from service.dtos.base_dto import BaseDTO
    dto_dict = {"id": uuid.uuid4()}
    dto = BaseDTO().from_dict(dto_dict)
    assert isinstance(dto, BaseDTO)
    assert isinstance(dto.id, uuid.UUID)
    assert {"id": dto.id} == dto_dict


def test_base_dto_as_serialized_dict():
    from service.dtos.base_dto import BaseDTO
    dto_dict = {"id": uuid.uuid4()}
    dto = BaseDTO().from_dict(dto_dict)
    expected_result = {"id": str(dto_dict["id"])}
    assert dto.as_serialized_dict() == expected_result
