import logging
from copy import copy
from typing import List

from service.dtos.dataset_aggregates_dto import DatasetAggregatesDTO
from service.infrastructure.dataset_aggregates_repository_interface import (
    DatasetAggregatesRepositoryInterface
)


class CacheDatasetAggregatesRepository(DatasetAggregatesRepositoryInterface):
    _singleton = None
    _datasets_aggregates_by_name_and_date = {}

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self: object):
        logging.debug("CacheDatasetAggregatesRepository()")

    def add_dataset_aggregates(
        self: object, dataset_aggregates_dto: DatasetAggregatesDTO
    ) -> None:
        logging.debug(
            "CacheDatasetAggregatesRepository."
            f"add_dataset_aggregates(dataset_aggregates_dto={dataset_aggregates_dto})"
        )
        self._datasets_aggregates_by_name_and_date[
            (dataset_aggregates_dto.name, dataset_aggregates_dto.created_date)
        ] = dataset_aggregates_dto

    def find_datasets_aggregates(self: object) -> List[DatasetAggregatesDTO]:
        logging.debug("CacheDatasetAggregatesRepository.find_datasets_aggregates()")
        return [
            copy(value) for _, value in self._datasets_aggregates_by_name_and_date.items()
        ]

    def reset(self: object) -> None:
        logging.debug("CacheDatasetAggregatesRepository.reset()")
        self._datasets_aggregates_by_name_and_date = {}
