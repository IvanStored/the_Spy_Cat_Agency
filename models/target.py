from sqlalchemy import ForeignKey, UUID, String, Text, Boolean
from sqlalchemy.orm import mapped_column, relationship

from models import BaseModel


class Target(BaseModel):
    __tablename__ = "targets"

    mission_id = mapped_column(UUID, ForeignKey("missions.id"))
    name = mapped_column(String)
    country = mapped_column(String)
    notes = mapped_column(Text)
    complete = mapped_column(Boolean, default=False)

    mission = relationship("Mission", back_populates="targets")
