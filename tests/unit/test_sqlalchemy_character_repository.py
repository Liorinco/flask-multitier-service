from copy import deepcopy


def test_SQLAlchemyCharacterRepository_instanciation(sqlalchemy_client):
    from service.infrastructure.sqlalchemy_character_repository import (
        SQLAlchemyCharacterRepository,
    )
    repository = SQLAlchemyCharacterRepository(sqlalchemy_client=sqlalchemy_client)

    assert isinstance(repository, SQLAlchemyCharacterRepository)
    import sqlalchemy
    assert isinstance(repository.db_session, sqlalchemy.orm.session.Session)


def test_repository_add_character(character_dto, character_repository):
    returned_value = character_repository.add_character(character_dto=character_dto)

    assert returned_value is None
    character_dtos = character_repository.find_characters()
    assert character_dtos == [character_dto]


def test_repository_find_characters(persisted_character_dto, character_repository):
    character_dtos = character_repository.find_characters()

    assert character_dtos == [persisted_character_dto]


def test_repository_find_character_by_id(persisted_character_dto, character_repository):
    character_dtos = character_repository.find_character_by_id(
        character_id=persisted_character_dto.id
    )

    assert character_dtos == persisted_character_dto


def test_repository_find_characters_without_data(character_repository):
    character_dtos = character_repository.find_characters()

    assert character_dtos == []


def test_repository_update_character(persisted_character_dto, character_repository):
    updated_character_dto = deepcopy(persisted_character_dto)
    updated_character_dto.name = "updated_" + persisted_character_dto.name
    updated_character_dto.age = persisted_character_dto.age + 3
    updated_character_dto.weight = persisted_character_dto.weight + 8.6
    updated_character_dto.is_human = not persisted_character_dto.is_human
    returned_value = character_repository.update_character(
        character_dto=updated_character_dto
    )

    assert returned_value is None
    character_dtos = character_repository.find_characters()
    assert character_dtos == [updated_character_dto]


def test_repository_delete_character_by_id(
    persisted_character_dto_population, character_repository
):
    persisted_character_dto = persisted_character_dto_population.pop()
    returned_value = character_repository.delete_character_by_id(
        character_id=persisted_character_dto.id
    )

    assert returned_value is None
    character_dtos = character_repository.find_characters()
    assert character_dtos == sorted(
        persisted_character_dto_population, key=lambda character_dto: character_dto.id
    )


def test_repository_reset(persisted_character_dto_population, character_repository):
    returned_value = character_repository.reset()

    assert returned_value is None
    character_dtos = character_repository.find_characters()
    assert character_dtos == []
