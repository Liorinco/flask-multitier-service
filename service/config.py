import logging
import os

from service.api.flask_application import FlaskApplication
from service.domain.character_management import CharacterManagement
from service.domain.dataset_management import DatasetManagement
from service.domain.garment_management import GarmentManagement
from service.infrastructure.cache_dataset_aggregates_repository import (
    CacheDatasetAggregatesRepository
)
from service.infrastructure.sqlalchemy_character_repository import (
    SQLAlchemyCharacterRepository
)
from service.infrastructure.sqlalchemy_data_repository import SQLAlchemyDataRepository
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
    data_repository = SQLAlchemyDataRepository(sqlalchemy_client=database_client)
    dataset_aggregates_repository = CacheDatasetAggregatesRepository()
    garment_repository = SQLAlchemyGarmentRepository(sqlalchemy_client=database_client)
    character_management_domain = CharacterManagement(
        repository=character_repository, garment_repository=garment_repository
    )
    dataset_management_domain = DatasetManagement(
        data_repository=data_repository,
        dataset_aggregates_repository=dataset_aggregates_repository
    )
    garment_management_domain = GarmentManagement(repository=garment_repository)
    return FlaskApplication(
        host=SERVICE_HOST,
        port=SERVICE_PORT,
        character_domain=character_management_domain,
        dataset_domain=dataset_management_domain,
        garment_domain=garment_management_domain,
        debug=SERVICE_DEBUG,
    )
