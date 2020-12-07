from typing import Any


def is_uuid(value: Any) -> bool:
    import uuid
    try:
        uuid.UUID(str(value))
    except ValueError:
        return False
    return True
