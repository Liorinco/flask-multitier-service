import uuid

from datetime import datetime

from service.dtos.data_dto import DataDTO
from service.dtos.dataset_dto import DataSetDTO


def test_dataset_dto_instance(dataset_dict):
    dto = DataSetDTO().from_dict(dataset_dict)
    assert isinstance(dto, DataSetDTO)
    assert isinstance(dto.id, uuid.UUID)
    assert isinstance(dto.created_date, datetime)
    assert isinstance(dto.aggregates, dict)
    assert isinstance(dto.dataset, list)
    assert False not in map(lambda x: isinstance(x, DataDTO), dto.dataset)
    assert {
        "id": dto.id,
        "created_date": dto.created_date,
        "aggregates": dto.aggregates,
        "dataset": dto.dataset,
    } == dataset_dict


def test_dataset_dto_asdict(dataset_dict):
    dto = DataSetDTO().from_dict(dataset_dict)
    expected_result = dataset_dict.copy()
    expected_result["dataset"] = [data.asdict() for data in expected_result["dataset"]]
    assert dto.asdict() == expected_result


def test_dataset_dto_as_serialized_dict(dataset_dict):
    dto = DataSetDTO().from_dict(dataset_dict)
    expected_result = dataset_dict.copy()
    expected_result["id"] = str(expected_result["id"])
    expected_result["created_date"] = expected_result["created_date"].isoformat()
    expected_result["dataset"] = [
        data.as_serialized_dict() for data in expected_result["dataset"]
    ]
    assert dto.as_serialized_dict() == expected_result
