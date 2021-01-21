import uuid
from typing import Optional

import pydantic


class POSTCharactersInput(pydantic.BaseModel):
    """Create character input."""
    character_name: str = pydantic.Field(
        default=..., description="Character's name", example="Zack"
    )
    character_age: int = pydantic.Field(
        default=..., description="Character's age", example=9
    )
    character_weight: float = pydantic.Field(
        default=..., description="Character's weight", example=37.9
    )
    character_is_human: bool = pydantic.Field(
        default=..., description="Character's kind", example=True
    )
    character_hat_id: Optional[uuid.UUID] = pydantic.Field(
        default=...,
        description="Hat worn by the character",
        example="fc9a56b5-74ba-4a4a-a1fb-11fcea49fffb"
    )


PUTCharactersInput = POSTCharactersInput
