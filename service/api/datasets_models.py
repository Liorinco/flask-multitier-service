from typing import List

import pydantic


class Data(pydantic.BaseModel):
    """Model of a data."""
    data_name: str = pydantic.Field(
        default=..., description="Name associated to the data", example="Zack"
    )
    data_value: float = pydantic.Field(
        default=..., description="Value associated to the data", example=17.3
    )


class POSTDatasetsInput(pydantic.BaseModel):
    """Create dataset input."""
    dataset: List[Data]
