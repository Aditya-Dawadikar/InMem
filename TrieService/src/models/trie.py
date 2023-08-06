from pydantic import BaseModel
from typing import Union

class InsertDataRequest(BaseModel):
    key: str
    value: Union [str, dict, list]