def test_character_dao_instanciation(character_dict):
    from service.infrastructure.daos.character_dao import CharacterDAO
    character_dao = CharacterDAO(**character_dict)
    assert isinstance(character_dao, CharacterDAO)
    for key, value in character_dict.items():
        assert key in character_dao.__dict__
        assert getattr(character_dao, key) == value


def test_character_dao_from_dto(character_dto):
    from service.infrastructure.daos.character_dao import CharacterDAO
    character_dao = CharacterDAO.from_dto(character_dto=character_dto)
    assert isinstance(character_dao, CharacterDAO)
    for key, value in character_dto.asdict().items():
        assert key in character_dao.__dict__
        assert getattr(character_dao, key) == value


def test_character_dao_asdict(character_dict):
    from service.infrastructure.daos.character_dao import CharacterDAO
    character_dao = CharacterDAO(**character_dict)
    assert character_dao.asdict() == character_dict


def test_character_dao_to_dto(character_dto):
    from service.infrastructure.daos.character_dao import CharacterDAO
    character_dao = CharacterDAO.from_dto(character_dto=character_dto)
    assert character_dao.to_dto() == character_dto
