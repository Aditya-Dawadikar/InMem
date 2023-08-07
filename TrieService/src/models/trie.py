from pydantic import BaseModel
from typing import Union

class InsertDataRequest(BaseModel):
    key: str
    value: Union [str, dict, list]

class InsertDocumentRequest(BaseModel):
    value: Union [dict, list]