from abc import ABC, abstractmethod
from typing import List

from service.dtos.dataset_aggregates_dto import DatasetAggregatesDTO


class DatasetAggregatesRepositoryInterface(ABC):
    @abstractmethod
    def add_dataset_aggregates(self: object, dataset_dto: DatasetAggregatesDTO) -> None:
        pass

    @abstractmethod
    def find_datasets_aggregates(self: object) -> List[DatasetAggregatesDTO]:
        pass

    @abstractmethod
    def reset(self: object) -> None:
        pass
