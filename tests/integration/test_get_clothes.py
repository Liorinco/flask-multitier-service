def test_find_clothes_without_data(client):
    response = client.get("/clothes")

    assert response.status_code == 200
    assert "clothes" in response.json
    assert response.json["clothes"] == []


def test_find_clothes(client, persisted_garment_dto_population):
    response = client.get("/clothes")

    assert response.status_code == 200
    expected_response = {
        "clothes": sorted(
            [
                garment_dto.as_serialized_dict()
                for garment_dto in persisted_garment_dto_population
            ],
            key=lambda garment_dict: garment_dict["id"])
    }
    assert response.json == expected_response
