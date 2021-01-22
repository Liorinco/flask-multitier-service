class NotExpectedValueError(ValueError):
    def __init__(
        self: object,
        variable_name: str,
        expected_type: type,
        given_type: type,
        message_detail: str = None
    ) -> object:
        error_message = (
            f"`{variable_name}` expects `{expected_type}`, but `{given_type}` is given"
        )
        error_message += f" ({message_detail})" if message_detail else ""
        super().__init__(error_message)


class Conflict(ValueError):
    def __init__(self: object, error_message: str) -> object:
        super().__init__(error_message)
