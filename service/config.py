import logging
import os

from service.api.flask_application import FlaskApplication
from service.domain.character_management import CharacterManagement
from service.domain.garment_management import GarmentManagement
from service.infrastructure.sqlalchemy_character_repository import (
    SQLAlchemyCharacterRepository
)
from service.infrastructure.sqlalchemy_garment_repository import (
    SQLAlchemyGarmentRepository
)
from service.infrastructure.sqlalchemy_client import SQLAlchemyClient


SERVICE_HOST = os.environ["SERVICE_HOST"]
SERVICE_PORT = int(os.environ["SERVICE_PORT"])
SERVICE_DEBUG = os.environ["SERVICE_DEBUG"]
DATABASE_URI = os.environ["DATABASE_URI"]


def configure_application():
    logging.basicConfig(level=logging.DEBUG)
    database_client = SQLAlchemyClient(database_uri=DATABASE_URI)
    character_repository = SQLAlchemyCharacterRepository(
        sqlalchemy_client=database_client
    )
    garment_repository = SQLAlchemyGarmentRepository(sqlalchemy_client=database_client)
    character_management_domain = CharacterManagement(
        repository=character_repository, garment_repository=garment_repository
    )
    garment_management_domain = GarmentManagement(repository=garment_repository)
    return FlaskApplication(
        host=SERVICE_HOST,
        port=SERVICE_PORT,
        character_domain=character_management_domain,
        garment_domain=garment_management_domain,
        debug=SERVICE_DEBUG,
    )
