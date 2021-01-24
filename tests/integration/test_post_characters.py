import uuid

from tests import tools


def test_create_character(client, character_dto, character_repository):
    expected_character_dict = character_dto.as_serialized_dict()
    payload = {
        "character_name": expected_character_dict["name"],
        "character_age": expected_character_dict["age"],
        "character_weight": expected_character_dict["weight"],
        "character_is_human": expected_character_dict["is_human"],
        "character_hat_id": expected_character_dict["hat_id"],
    }
    response = client.post("/characters", json=payload)

    assert response.status_code == 200
    assert "character_id" in response.json
    retrieved_character_uuid = response.json["character_id"]
    assert tools.is_uuid(retrieved_character_uuid)
    character_dtos = character_repository.find_characters()
    character_dto.id = uuid.UUID(retrieved_character_uuid)
    assert character_dtos == [character_dto]


def test_create_human_with_hat(
    client, character_dto, persisted_garment_dto, character_repository
):
    character_dto.hat_id = persisted_garment_dto.id
    expected_character_dict = character_dto.as_serialized_dict()
    payload = {
        "character_name": expected_character_dict["name"],
        "character_age": expected_character_dict["age"],
        "character_weight": expected_character_dict["weight"],
        "character_is_human": expected_character_dict["is_human"],
        "character_hat_id": expected_character_dict["hat_id"],
    }
    response = client.post("/characters", json=payload)

    assert response.status_code == 200
    assert "character_id" in response.json
    retrieved_character_uuid = response.json["character_id"]
    assert tools.is_uuid(retrieved_character_uuid)
    character_dtos = character_repository.find_characters()
    character_dto.id = uuid.UUID(retrieved_character_uuid)
    assert character_dtos == [character_dto]


def test_create_non_human_with_hat(
    client, character_dict, persisted_garment_dto, character_repository
):
    character_dict["hat_id"] = persisted_garment_dto.id
    payload = {
        "character_name": character_dict["name"],
        "character_age": character_dict["age"],
        "character_weight": character_dict["weight"],
        "character_is_human": False,
        "character_hat_id": character_dict["hat_id"],
    }
    response = client.post("/characters", json=payload)

    assert response.status_code == 409
    assert response.data == b"Only humans can wear hats"


def test_create_young_human_too_big(
    client, character_dict, persisted_garment_dto, character_repository
):
    age_limit = 10
    weight_limit = 80.
    character_dict["hat_id"] = persisted_garment_dto.id
    payload = {
        "character_name": character_dict["name"],
        "character_age": age_limit,
        "character_weight": weight_limit + 0.1,
        "character_is_human": True,
        "character_hat_id": character_dict["hat_id"],
    }
    response = client.post("/characters", json=payload)

    assert response.status_code == 409
    assert response.data.decode("utf-8") == (
        f"Humans under or {age_limit} years old cannot weigh more than {weight_limit} kg"
    )
