import uuid
from typing import Optional


from pydantic import BaseModel


class TargetSchema(BaseModel):
    name: str
    country: str
    notes: str
    complete: bool = False


class TargetReadSchema(BaseModel):
    id: uuid.UUID
    name: str
    country: str
    notes: str
    complete: bool


class TargetUpdateSchema(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    notes: Optional[str]
    complete: Optional[bool] = None
