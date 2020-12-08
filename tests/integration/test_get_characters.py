def test_find_characters_without_data(client):
    response = client.get("/characters")

    assert response.status_code == 200
    assert "characters" in response.json
    assert response.json["characters"] == []


def test_find_characters(client, persisted_character_dto_population):
    response = client.get("/characters")

    assert response.status_code == 200
    expected_response = {
        "characters": sorted(
            [
                character_dto.as_serialized_dict()
                for character_dto in persisted_character_dto_population
            ],
            key=lambda character_dict: character_dict["id"])
    }
    assert response.json == expected_response
