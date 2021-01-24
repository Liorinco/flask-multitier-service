import uuid


def test_repository_find_characters_by_hat_id_with_existing_association(
    character_repository, persisted_human_with_hat_dto
):
    dtos = character_repository.find_characters_by_hat_id(
        hat_id=persisted_human_with_hat_dto.hat_id
    )
    assert dtos == [persisted_human_with_hat_dto]


def test_repository_find_characters_by_hat_id_with_non_existent_association(
    character_repository, persisted_character_dto
):
    dtos = character_repository.find_characters_by_hat_id(hat_id=uuid.uuid4())
    assert dtos == []
