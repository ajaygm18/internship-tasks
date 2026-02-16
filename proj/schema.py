from pydantic import BaseModel, ConfigDict
from typing import Optional


class Candidate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    age: int
    education: str
    previousCTC: Optional[float] = None
    experience: Optional[int] = None


class showCandidate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    age: int
    education: str
    previousCTC: Optional[float] = None
    experience: Optional[int] = None


class Admin(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    age: int


