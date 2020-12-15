def test_find_garment(client, persisted_garment_dto):
    expected_garment = persisted_garment_dto.as_serialized_dict()
    response = client.get(f"/clothes/{expected_garment['id']}")

    assert response.status_code == 200
    assert response.json == expected_garment
