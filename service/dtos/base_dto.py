import uuid

from service.exceptions import NotExpectedValueError


class BaseDTO:
    @property
    def id(self: object) -> uuid.UUID:
        return self.__id

    @id.setter
    def id(self: object, id: uuid.UUID) -> None:
        if isinstance(id, uuid.UUID):
            self.__id = id
        elif isinstance(id, str):
            self.__id = uuid.UUID(id)
        else:
            raise NotExpectedValueError(
                variable_name="id", expected_type=uuid.UUID, given_type=type(id)
            )

    def from_dict(self: object, dto_dict: dict):
        for key, value in dto_dict.items():
            setattr(self, key, value)
        return self

    def as_serialized_dict(self: object) -> dict:
        return {"id": str(self.__id)}
