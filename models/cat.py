from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, relationship

from models import BaseModel


class Cat(BaseModel):
    __tablename__ = "cats"

    name = mapped_column(String(20), nullable=False)
    years_of_exp = mapped_column(Integer, nullable=False)
    breed = mapped_column(String, nullable=False)
    salary = mapped_column(Integer, nullable=False)

    missions = relationship("Mission", back_populates="cat")
