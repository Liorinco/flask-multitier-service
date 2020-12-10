import uuid


def test_garment_dto_instance(garment_dict):
    from service.dtos.color import Color
    from service.dtos.garment_dto import GarmentDTO
    dto = GarmentDTO().from_dict(garment_dict)
    assert isinstance(dto, GarmentDTO)
    assert isinstance(dto.id, uuid.UUID)
    assert isinstance(dto.color, Color)
    assert {"id": dto.id, "color": dto.color} == garment_dict


def test_garment_dto_asdict(garment_dict):
    from service.dtos.garment_dto import GarmentDTO
    dto = GarmentDTO().from_dict(garment_dict)
    assert dto.asdict() == garment_dict


def test_garment_dto_as_serialized_dict(garment_dict):
    from service.dtos.garment_dto import GarmentDTO
    dto = GarmentDTO().from_dict(garment_dict)
    expected_result = garment_dict.copy()
    expected_result["id"] = str(expected_result["id"])
    expected_result["color"] = expected_result["color"].value
    assert dto.as_serialized_dict() == expected_result
