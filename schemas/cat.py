from typing import Optional
import uuid

from pydantic import BaseModel


class CatCreateSchema(BaseModel):
    name: str
    years_of_exp: int
    breed: str
    salary: int


class CatReadSchema(BaseModel):
    id: uuid.UUID
    name: str
    years_of_exp: int
    breed: str
    salary: int


class CatUpdateSchema(BaseModel):
    name: Optional[str] = None
    years_of_exp: Optional[int] = None
    salary: Optional[int] = None


class CatListSchema(BaseModel):
    cats: list[CatReadSchema]
