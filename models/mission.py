from sqlalchemy import Boolean, UUID, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column

from models import BaseModel


class Mission(BaseModel):
    __tablename__ = "missions"

    cat_uuid = mapped_column(UUID, ForeignKey("cats.id"), nullable=True)
    is_completed = mapped_column(Boolean, default=False)

    cat = relationship("Cat", back_populates="missions", uselist=False)
    targets = relationship("Target", back_populates="mission")

    __table_args__ = (
        UniqueConstraint("cat_uuid", name="unique_mission_per_cat"),
    )
