from service.dtos.character_dto import CharacterDTO


def test_update_character(
    client, persisted_character_dto, persisted_garment_dto, character_repository
):
    new_character_payload = {
        "character_name": "updated_" + persisted_character_dto.name,
        "character_age": 3 + persisted_character_dto.age,
        "character_weight": 3. + persisted_character_dto.weight,
        "character_is_human": not persisted_character_dto.is_human,
        "character_hat_id": persisted_garment_dto.id,
    }
    response = client.put(
        f"/characters/{(persisted_character_dto.id)}", json=new_character_payload
    )

    assert response.status_code == 200
    assert response.json is None
    expected_character_dto = CharacterDTO().from_dict({
        "id": persisted_character_dto.id,
        "name": new_character_payload["character_name"],
        "age": new_character_payload["character_age"],
        "weight": new_character_payload["character_weight"],
        "is_human": new_character_payload["character_is_human"],
        "hat_id": new_character_payload["character_hat_id"],
    })
    assert character_repository.find_characters() == [expected_character_dto]


def test_update_non_human_to_wear_hat(
    client, persisted_character_dto, persisted_garment_dto, character_repository
):
    new_character_payload = {
        "character_name": persisted_character_dto.name,
        "character_age": persisted_character_dto.age,
        "character_weight": persisted_character_dto.weight,
        "character_is_human": persisted_character_dto.is_human,
        "character_hat_id": persisted_garment_dto.id,
    }
    response = client.put(
        f"/characters/{(persisted_character_dto.id)}", json=new_character_payload
    )

    assert response.status_code == 409
    assert response.data == b"Only humans can wear hats"


def test_update_young_human_too_big(
    client, persisted_character_dto, character_repository
):
    age_limit = 10
    weight_limit = 80.
    new_character_payload = {
        "character_name": persisted_character_dto.name,
        "character_age": age_limit,
        "character_weight": weight_limit + 0.1,
        "character_is_human": True,
        "character_hat_id": persisted_character_dto.hat_id,
    }
    response = client.put(
        f"/characters/{(persisted_character_dto.id)}", json=new_character_payload
    )

    assert response.status_code == 409
    assert response.data.decode("utf-8") == (
        f"Humans under or {age_limit} years old cannot weigh more than {weight_limit} kg"
    )


def test_update_character_with_negative_age(
    client, persisted_character_dto, character_repository
):
    age = -1
    new_character_payload = {
        "character_name": persisted_character_dto.name,
        "character_age": age,
        "character_weight": persisted_character_dto.weight,
        "character_is_human": persisted_character_dto.is_human,
        "character_hat_id": persisted_character_dto.hat_id,
    }
    response = client.put(
        f"/characters/{(persisted_character_dto.id)}", json=new_character_payload
    )

    assert response.status_code == 422
    assert response.data.decode("utf-8") == (
        f"`age` expects `{type(age)}`, but `{type(age)}` is given (must be positive)"
    )
