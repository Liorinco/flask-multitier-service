def test_entity_repository_instanciation(sqlalchemy_client, entity_factory):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)

    assert isinstance(repository, entity_factory.repository_class)


def test_repository_add_entity(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    dto = entity_factory.generate_dto()
    add_entity = getattr(repository, entity_factory.repository_add_entity_method_name)
    returned_value = add_entity(dto)

    assert returned_value is None
    dtos = entity_factory.find_persisted_dtos(sqlalchemy_client=sqlalchemy_client)
    assert dtos == [dto]


def test_repository_find_entities(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    persisted_dto = entity_factory.generate_persisted_dto(
        sqlalchemy_client=sqlalchemy_client
    )
    find_entities = getattr(
        repository, entity_factory.repository_find_entities_method_name
    )
    dtos = find_entities()

    assert dtos == [persisted_dto]


def test_repository_find_entity_by_id(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    persisted_dto = entity_factory.generate_persisted_dto(
        sqlalchemy_client=sqlalchemy_client
    )
    find_entity_by_id = getattr(
        repository, entity_factory.repository_find_entity_by_id_method_name
    )
    dtos = find_entity_by_id(persisted_dto.id)

    assert dtos == persisted_dto


def test_repository_find_entities_without_data(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    find_entities = getattr(
        repository, entity_factory.repository_find_entities_method_name
    )
    dtos = find_entities()

    assert dtos == []


def test_repository_update_entity(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    persisted_dto = entity_factory.generate_persisted_dto(
        sqlalchemy_client=sqlalchemy_client
    )
    updated_dto = entity_factory.generate_entity_update(entity_dto=persisted_dto)
    update_entity = getattr(
        repository, entity_factory.repository_update_entity_method_name
    )
    returned_value = update_entity(updated_dto)

    assert returned_value is None
    dtos = entity_factory.find_persisted_dtos(sqlalchemy_client=sqlalchemy_client)
    assert dtos == [updated_dto]


def test_repository_delete_entity_by_id(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    persisted_dto = entity_factory.generate_persisted_dto(
        sqlalchemy_client=sqlalchemy_client
    )
    delete_entity_by_id = getattr(
        repository, entity_factory.repository_delete_entity_by_id_method_name
    )
    returned_value = delete_entity_by_id(persisted_dto.id)

    assert returned_value is None
    dtos = entity_factory.find_persisted_dtos(sqlalchemy_client=sqlalchemy_client)
    assert dtos == []


def test_repository_reset(entity_factory, sqlalchemy_client):
    repository = entity_factory.repository_class(sqlalchemy_client=sqlalchemy_client)
    entity_factory.generate_persisted_dto(sqlalchemy_client=sqlalchemy_client)
    reset_entities = getattr(
        repository, entity_factory.repository_reset_entities_method_name
    )
    returned_value = reset_entities()

    assert returned_value is None
    dtos = entity_factory.find_persisted_dtos(sqlalchemy_client=sqlalchemy_client)
    assert dtos == []
