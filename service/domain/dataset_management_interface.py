from abc import ABC, abstractmethod
from typing import Dict, List, Union


class DatasetManagementInterface(ABC):
    @abstractmethod
    def register_dataset(
        self: object, dataset: List[Dict[str, Union[str, float]]]
    ) -> None:
        pass
