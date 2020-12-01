class NotExpectedValueError(ValueError):
    def __init__(
        self: object, variable_name: str, expected_type: type, given_type: type
    ) -> object:
        super().__init__(
            f"`{variable_name}` set with `{expected_type}`, "
            f"but `{given_type}` is expected"
        )
