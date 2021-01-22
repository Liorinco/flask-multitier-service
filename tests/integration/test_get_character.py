def test_find_character(client, persisted_character_dto):
    expected_character = persisted_character_dto.as_serialized_dict()
    response = client.get(f"/characters/{expected_character['id']}")

    assert response.status_code == 200
    assert response.json == expected_character


def test_find_character_with_hat(client, persisted_human_with_hat_dto):
    expected_character = persisted_human_with_hat_dto.as_serialized_dict()
    response = client.get(f"/characters/{expected_character['id']}")

    assert response.status_code == 200
    assert response.json == expected_character
