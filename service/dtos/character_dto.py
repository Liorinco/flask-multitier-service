from service.exceptions import NotExpectedValueError
from service.dtos.base_dto import BaseDTO


class CharacterDTO(BaseDTO):
    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, name: str) -> None:
        if isinstance(name, str):
            self.__name = name
        else:
            raise NotExpectedValueError(
                variable_name="name", expected_type=str, given_type=type(name)
            )

    @property
    def age(self: object) -> int:
        return self.__age

    @age.setter
    def age(self: object, age: int) -> None:
        if isinstance(age, int):
            self.__age = age
        else:
            raise NotExpectedValueError(
                variable_name="age", expected_type=int, given_type=type(age)
            )

    @property
    def weight(self: object) -> float:
        return self.__weight

    @weight.setter
    def weight(self: object, weight: float) -> None:
        if isinstance(weight, float):
            self.__weight = weight
        else:
            raise NotExpectedValueError(
                variable_name="weight", expected_type=float, given_type=type(weight)
            )

    @property
    def is_human(self: object) -> bool:
        return self.__is_human

    @is_human.setter
    def is_human(self: object, is_human: bool) -> None:
        if isinstance(is_human, bool):
            self.__is_human = is_human
        else:
            raise NotExpectedValueError(
                variable_name="is_human", expected_type=bool, given_type=type(is_human)
            )

    @property
    def is_human(self: object) -> bool:
        return self.__is_human

    @is_human.setter
    def is_human(self: object, is_human: bool) -> None:
        if isinstance(is_human, bool):
            self.__is_human = is_human
        else:
            raise NotExpectedValueError(
                variable_name="is_human", expected_type=bool, given_type=type(is_human)
            )

    def asdict(self: object) -> dict:
        dto_dict = super().asdict()
        dto_dict.update({
            "name": self.__name,
            "age": self.__age,
            "weight": self.__weight,
            "is_human": self.__is_human,
        })
        return dto_dict

    def as_serialized_dict(self: object) -> dict:
        serialized_dict = super().as_serialized_dict()
        serialized_dict.update({
            "name": self.__name,
            "age": self.__age,
            "weight": self.__weight,
            "is_human": self.__is_human,
        })
        return serialized_dict
