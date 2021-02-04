from copy import copy


def test_create_dataset(client, data_repository, dataset_aggregates_repository):
    payload = {
        "dataset": [
            {"data_name": "anna", "data_value": 10.3},
            {"data_name": "kevin", "data_value": 3.9},
            {"data_name": "henri", "data_value": 6.},
            {"data_name": "kevin", "data_value": 17.2},
            {"data_name": "kevin", "data_value": 12.8},
            {"data_name": "anna", "data_value": 11.},
            {"data_name": "anna", "data_value": 9.5},
        ]
    }
    response = client.post("/datasets", json=payload)

    assert response.status_code == 201
    assert response.json is None
    # Check data are stored
    expected_data = copy(payload["dataset"])
    data_dtos = data_repository.find_data()
    for data_dto in data_dtos:
        data = {"data_name": data_dto.name, "data_value": data_dto.value}
        assert data in expected_data
        expected_data.remove(data)
    assert expected_data == []
    # Check dataset aggregates are stored
    expected_data = copy(payload["dataset"])
    dataset_aggregates_dtos = dataset_aggregates_repository.find_datasets_aggregates()
    expected_names = set([data["data_name"] for data in expected_data])
    for dataset_aggregates_dto in dataset_aggregates_dtos:
        assert dataset_aggregates_dto.name in expected_names
        expected_names.remove(dataset_aggregates_dto.name)
    assert expected_names == set()
