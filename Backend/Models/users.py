from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id_Emp:Optional[int]=None
