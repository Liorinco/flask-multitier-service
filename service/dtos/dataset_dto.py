from datetime import datetime
from typing import List

from service.exceptions import NotExpectedValueError
from service.dtos.base_dto import BaseDTO
from service.dtos.data_dto import DataDTO


class DataSetDTO(BaseDTO):
    @property
    def created_date(self: object) -> datetime:
        return self.__created_date

    @created_date.setter
    def created_date(self: object, created_date: datetime) -> None:
        if not isinstance(created_date, datetime):
            raise NotExpectedValueError(
                variable_name="created_date",
                expected_type=datetime,
                given_type=type(created_date),
            )

        self.__created_date = created_date

    @property
    def aggregates(self: object) -> dict:
        return self.__aggregates

    @aggregates.setter
    def aggregates(self: object, aggregates: dict) -> None:
        if not isinstance(aggregates, dict):
            raise NotExpectedValueError(
                variable_name="aggregates",
                expected_type=dict,
                given_type=type(aggregates)
            )

        self.__aggregates = aggregates

    @property
    def dataset(self: object) -> List[DataDTO]:
        return self.__dataset

    @dataset.setter
    def dataset(self: object, dataset: List[DataDTO]) -> None:
        if (
            not isinstance(dataset, list) or
            False in map(lambda x: isinstance(x, DataDTO), dataset)
        ):
            raise NotExpectedValueError(
                variable_dataset="dataset",
                expected_type=List[DataDTO],
                given_type=type(dataset)
            )

        self.__dataset = dataset

    def asdict(self: object) -> dict:
        dto_dict = super().asdict()
        dto_dict.update({
            "created_date": self.__created_date,
            "aggregates": self.__aggregates,
            "dataset": [data.asdict() for data in self.__dataset],
        })
        return dto_dict

    def as_serialized_dict(self: object) -> dict:
        serialized_dict = super().as_serialized_dict()
        serialized_dict.update({
            "created_date": self.__created_date.isoformat(),
            "aggregates": self.__aggregates,
            "dataset": [data.as_serialized_dict() for data in self.__dataset],
        })
        return serialized_dict
