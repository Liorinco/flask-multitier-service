import uuid
from abc import ABC, abstractmethod
from typing import List

from service.dtos.dataset_dto import DataSetDTO


class DataSetRepositoryInterface(ABC):
    @abstractmethod
    def add_dataset(self: object, dataset_dto: DataSetDTO) -> None:
        pass

    @abstractmethod
    def find_dataset(self: object) -> List[DataSetDTO]:
        pass

    @abstractmethod
    def find_dataset_by_id(self: object, dataset_id: uuid.UUID) -> DataSetDTO:
        pass

    @abstractmethod
    def update_dataset(self: object, dataset_dto: DataSetDTO) -> None:
        pass

    @abstractmethod
    def delete_dataset_by_id(self: object, dataset_id: uuid.UUID) -> None:
        pass
