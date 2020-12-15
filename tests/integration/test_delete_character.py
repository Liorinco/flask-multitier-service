def test_remove_character(client, persisted_character_dto, character_repository):
    response = client.delete(f"/characters/{str(persisted_character_dto.id)}")

    assert response.status_code == 200
    assert response.json is None
    assert character_repository.find_characters() == []