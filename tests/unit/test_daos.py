import uuid


def test_character_dao_instanciation():
    from service.infrastructure.daos.character_dao import CharacterDAO
    character_dao = CharacterDAO(
        id=uuid.UUID,
        name="dumm_character_name",
        age=30,
        weight=70.3,
        is_human=True,
    )
    assert isinstance(character_dao, CharacterDAO)
