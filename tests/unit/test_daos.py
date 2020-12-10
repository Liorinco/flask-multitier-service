def test_dao_instanciation(entity):
    entity_dict = entity.generate_dict()
    dao = entity.dao_class(**entity_dict)
    assert isinstance(dao, entity.dao_class)
    for key, value in entity_dict.items():
        assert key in dao.__dict__
        assert getattr(dao, key) == value


def test_dao_from_dto(entity):
    dto = entity.generate_dto()
    dao = entity.dao_class.from_dto(dto)
    assert isinstance(dao, entity.dao_class)
    for key, value in dto.asdict().items():
        assert key in dao.__dict__
        assert getattr(dao, key) == value


def test_dao_asdict(entity):
    entity_dict = entity.generate_dict()
    dao = entity.dao_class(**entity_dict)
    assert dao.asdict() == entity_dict


def test_dao_to_dto(entity):
    dto = entity.generate_dto()
    dao = entity.dao_class.from_dto(dto)
    assert dao.to_dto() == dto
