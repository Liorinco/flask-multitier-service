from service.exceptions import NotExpectedValueError
from service.dtos.base_dto import BaseDTO
from service.dtos.color import Color


class GarmentDTO(BaseDTO):
    @property
    def color(self: object) -> str:
        return self.__color

    @color.setter
    def color(self: object, color: Color) -> None:
        if isinstance(color, Color):
            self.__color = color
        else:
            raise NotExpectedValueError(
                variable_name="color", expected_type=Color, given_type=type(color)
            )

    def asdict(self: object) -> dict:
        dto_dict = super().asdict()
        dto_dict.update({"color": self.__color})
        return dto_dict

    def as_serialized_dict(self: object) -> dict:
        serialized_dict = super().as_serialized_dict()
        serialized_dict.update({"color": self.__color.value})
        return serialized_dict
