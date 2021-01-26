import uuid
from abc import ABC, abstractmethod
from typing import List

from service.dtos.data_dto import DataDTO


class DataRepositoryInterface(ABC):
    @abstractmethod
    def add_data(self: object, data_dto: DataDTO) -> None:
        pass

    @abstractmethod
    def find_data(self: object) -> List[DataDTO]:
        pass

    @abstractmethod
    def find_data_by_id(self: object, data_id: uuid.UUID) -> DataDTO:
        pass

    @abstractmethod
    def update_data(self: object, data_dto: DataDTO) -> None:
        pass

    @abstractmethod
    def delete_data_by_id(self: object, data_id: uuid.UUID) -> None:
        pass
