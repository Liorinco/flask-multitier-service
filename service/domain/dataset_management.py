import logging
import uuid
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Union

from service.domain.dataset_management_interface import DatasetManagementInterface
from service.dtos.data_dto import DataDTO
from service.dtos.dataset_aggregates_dto import DatasetAggregatesDTO
from service.infrastructure.data_repository_interface import DataRepositoryInterface
from service.infrastructure.dataset_aggregates_repository_interface import (
    DatasetAggregatesRepositoryInterface
)


class DatasetManagement(DatasetManagementInterface):
    def __init__(
        self: object,
        data_repository: DataRepositoryInterface,
        dataset_aggregates_repository: DatasetAggregatesRepositoryInterface
    ):
        logging.debug("DatasetManagement.__init__")
        self._data_repository = data_repository
        self._dataset_aggregates_repository = dataset_aggregates_repository

    def register_dataset(
        self: object, dataset: List[Dict[str, Union[str, float]]]
    ) -> None:
        logging.debug("DatasetManagement.register_dataset")
        created_date = datetime.now()
        datasets_by_name = defaultdict(list)
        for data in dataset:
            data_dto = DataDTO().from_dict(
                {
                    "id": uuid.uuid4(),
                    "created_date": created_date,
                    "name": data["data_name"],
                    "value": data["data_value"]
                }
            )
            self._data_repository.add_data(data_dto=data_dto)
            datasets_by_name[data["data_name"]].append(data["data_value"])
        for data_name, dataset_by_name in datasets_by_name.items():
            dataset_aggregates_dto = DatasetAggregatesDTO().from_dict(
                {
                    "created_date": created_date,
                    "name": data_name,
                    "average": sum(dataset_by_name) / len(dataset_by_name)
                }
            )
            self._dataset_aggregates_repository.add_dataset_aggregates(
                dataset_aggregates_dto
            )
