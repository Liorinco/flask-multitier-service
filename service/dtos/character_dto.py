import uuid
from typing import Optional

from service.exceptions import Conflict, NotExpectedValueError
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
        if not isinstance(age, int):
            raise NotExpectedValueError(
                variable_name="age", expected_type=int, given_type=type(age)
            )

        self._raise_conflict_if_young_human_is_too_big(age=age)
        self.__age = age

    @property
    def weight(self: object) -> float:
        return self.__weight

    @weight.setter
    def weight(self: object, weight: float) -> None:
        if not isinstance(weight, float):
            raise NotExpectedValueError(
                variable_name="weight", expected_type=float, given_type=type(weight)
            )

        self._raise_conflict_if_young_human_is_too_big(weight=weight)
        self.__weight = weight

    @property
    def is_human(self: object) -> bool:
        return self.__is_human

    @is_human.setter
    def is_human(self: object, is_human: bool) -> None:
        if not isinstance(is_human, bool):
            raise NotExpectedValueError(
                variable_name="is_human", expected_type=bool, given_type=type(is_human)
            )

        self._raise_conflict_if_non_human_wears_hat(is_human=is_human)
        self._raise_conflict_if_young_human_is_too_big(is_human=is_human)
        self.__is_human = is_human

    @property
    def hat_id(self: object) -> uuid.UUID:
        return self.__hat_id

    @hat_id.setter
    def hat_id(self: object, hat_id: uuid.UUID) -> None:
        if not (hat_id is None or isinstance(hat_id, uuid.UUID)):
            raise NotExpectedValueError(
                variable_name="hat_id",
                expected_type=Optional[uuid.UUID],
                given_type=type(hat_id),
            )

        self._raise_conflict_if_non_human_wears_hat(hat_id=hat_id)
        self.__hat_id = hat_id

    def asdict(self: object) -> dict:
        dto_dict = super().asdict()
        dto_dict.update({
            "name": self.__name,
            "age": self.__age,
            "weight": self.__weight,
            "is_human": self.__is_human,
            "hat_id": self.__hat_id,
        })
        return dto_dict

    def as_serialized_dict(self: object) -> dict:
        serialized_dict = super().as_serialized_dict()
        serialized_dict.update({
            "name": self.__name,
            "age": self.__age,
            "weight": self.__weight,
            "is_human": self.__is_human,
            "hat_id": None if self.__hat_id is None else str(self.__hat_id),
        })
        return serialized_dict

    def _raise_conflict_if_non_human_wears_hat(
        self, *, is_human=Ellipsis, hat_id=Ellipsis
    ):
        if is_human is Ellipsis and hasattr(self, "_CharacterDTO__is_human"):
            is_human = self.__is_human
        if hat_id is Ellipsis and hasattr(self, "_CharacterDTO__hat_id"):
            hat_id = self.__hat_id
        if not (
            (not hasattr(self, "_CharacterDTO__is_human") and is_human is Ellipsis) or
            (not hasattr(self, "_CharacterDTO__hat_id") and hat_id is Ellipsis) or
            is_human is True or
            hat_id is None
        ):
            raise Conflict(error_message="Only humans can wear hats")

    def _raise_conflict_if_young_human_is_too_big(
        self, *, is_human=Ellipsis, age=Ellipsis, weight=Ellipsis
    ):
        age_limit = 10
        weight_limit = 80.
        if is_human is Ellipsis and hasattr(self, "_CharacterDTO__is_human"):
            is_human = self.__is_human
        if age is Ellipsis and hasattr(self, "_CharacterDTO__age"):
            age = self.__age
        if weight is Ellipsis and hasattr(self, "_CharacterDTO__weight"):
            weight = self.__weight
        if not (
            (not hasattr(self, "_CharacterDTO__is_human") and is_human is Ellipsis) or
            (not hasattr(self, "_CharacterDTO__age") and age is Ellipsis) or
            (not hasattr(self, "_CharacterDTO__weight") and weight is Ellipsis) or
            is_human is False or
            age > age_limit or
            weight <= weight_limit
        ):
            raise Conflict(
                error_message=(
                    f"Humans under or {age_limit} years old "
                    f"cannot weigh more than {weight_limit} kg"
                )
            )
