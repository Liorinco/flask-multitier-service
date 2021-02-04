from datetime import datetime

from service.exceptions import NotExpectedValueError
from service.dtos.base_dto import BaseDTO


class DatasetAggregatesDTO(BaseDTO):
    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, name: str) -> None:
        if not isinstance(name, str):
            raise NotExpectedValueError(
                variable_name="name",
                expected_type=str,
                given_type=type(name),
            )

        self.__name = name

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
    def average(self: object) -> float:
        return self.__average

    @average.setter
    def average(self: object, average: float) -> None:
        if not isinstance(average, float):
            raise NotExpectedValueError(
                variable_name="average",
                expected_type=float,
                given_type=type(average)
            )

        self.__average = average

    def asdict(self: object) -> dict:
        dto_dict = super().asdict()
        dto_dict.update({
            "name": self.__name,
            "created_date": self.__created_date,
            "average": self.__average,
        })
        return dto_dict

    def as_serialized_dict(self: object) -> dict:
        serialized_dict = super().as_serialized_dict()
        serialized_dict.update({
            "name": self.__name,
            "created_date": self.__created_date.isoformat(),
            "average": self.__average,
        })
        return serialized_dict
