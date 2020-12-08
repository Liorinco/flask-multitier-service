from service.dtos.character_dto import CharacterDTO


def test_update_character(client, persisted_character_dto, character_repository):
    new_character = {
        "name": "updated_" + persisted_character_dto.name,
        "age": 3 + persisted_character_dto.age,
        "weight": 3. + persisted_character_dto.weight,
        "is_human": not persisted_character_dto.is_human,
    }
    response = client.put(
        f"/characters/{(persisted_character_dto.id)}", json=new_character
    )

    assert response.status_code == 200
    assert response.json is None
    new_character["id"] = persisted_character_dto.id
    expected_character_dto = CharacterDTO().from_dict(new_character)
    assert character_repository.find_characters() == [expected_character_dto]
