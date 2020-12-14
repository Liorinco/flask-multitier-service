def test_dao_instanciation(entity_factory):
    entity_dict = entity_factory.generate_dict()
    dao = entity_factory.dao_class(**entity_dict)
    assert isinstance(dao, entity_factory.dao_class)
    for key, value in entity_dict.items():
        assert key in dao.__dict__
        assert getattr(dao, key) == value


def test_dao_from_dto(entity_factory):
    dto = entity_factory.generate_dto()
    dao = entity_factory.dao_class.from_dto(dto)
    assert isinstance(dao, entity_factory.dao_class)
    for key, value in dto.asdict().items():
        assert key in dao.__dict__
        assert getattr(dao, key) == value


def test_dao_asdict(entity_factory):
    entity_dict = entity_factory.generate_dict()
    dao = entity_factory.dao_class(**entity_dict)
    assert dao.asdict() == entity_dict


def test_dao_to_dto(entity_factory):
    dto = entity_factory.generate_dto()
    dao = entity_factory.dao_class.from_dto(dto)
    assert dao.to_dto() == dto
