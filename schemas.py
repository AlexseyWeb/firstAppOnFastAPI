from pydantic import BaseModel
from typing import Optional

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STaskGet(STaskAdd):
    id: int

class SUser(BaseModel):
    name: str
    family: str
    sallary: Optional[float] = None
    job: str
