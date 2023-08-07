from pydantic import BaseModel

class CreateNewDB(BaseModel):
    db_name: str
    db_mode: str