def test_remove_garment(client, persisted_garment_dto, garment_repository):
    response = client.delete(f"/clothes/{str(persisted_garment_dto.id)}")

    assert response.status_code == 200
    assert response.json is None
    assert garment_repository.find_clothes() == []
