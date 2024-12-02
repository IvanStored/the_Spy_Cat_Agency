from typing import Optional
import uuid

from pydantic import BaseModel

from schemas.target import TargetSchema, TargetReadSchema


class MissionCreateSchema(BaseModel):
    cat_uuid: Optional[uuid.UUID] = None
    is_completed: bool = False
    targets: list[TargetSchema]


class MissionReadSchema(BaseModel):
    id: uuid.UUID
    cat_uuid: Optional[uuid.UUID] = None
    is_completed: bool = False
    targets: Optional[list[TargetReadSchema]] = None


class MissionListSchema(BaseModel):
    missions: list[MissionReadSchema]
