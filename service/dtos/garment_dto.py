from enum import Enum

from service.exceptions import NotExpectedValueError
from service.dtos.base_dto import BaseDTO
from service.dtos.color import Color


class GarmentArticle(Enum):
    HAT = "hat"


class GarmentDTO(BaseDTO):
    @property
    def article(self: object) -> GarmentArticle:
        return self.__article

    @article.setter
    def article(self: object, article: GarmentArticle) -> None:
        if isinstance(article, GarmentArticle):
            self.__article = article
        else:
            raise NotExpectedValueError(
                variable_name="article",
                expected_type=GarmentArticle,
                given_type=type(article)
            )

    @property
    def color(self: object) -> Color:
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
        dto_dict.update({"article": self.__article, "color": self.__color})
        return dto_dict

    def as_serialized_dict(self: object) -> dict:
        serialized_dict = super().as_serialized_dict()
        serialized_dict.update(
            {"article": self.__article.value, "color": self.__color.value}
        )
        return serialized_dict
