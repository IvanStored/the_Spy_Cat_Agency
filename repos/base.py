import uuid
from typing import Any

from sqlalchemy import insert, select, update, delete, Result, Sequence
from sqlalchemy.orm import Session


class BaseRepo:
    model = None

    def __init__(self, session: Session):
        self.session = session

    def get_by_uuid(self, uuid_: uuid.UUID) -> Result | Any:
        query = select(self.model).where(self.model.id == uuid_)
        res = self.session.execute(statement=query)
        return res.scalar_one()

    def list(self) -> Sequence:
        query = select(self.model)
        res = self.session.execute(statement=query)

        return res.scalars().all()

    def create_instance(self, instance_data: dict) -> Any:
        query = (
            insert(self.model).values(**instance_data).returning(self.model)
        )
        res = self.session.execute(statement=query)
        return res.scalar_one()

    def update_instance(self, uuid_: uuid.UUID, new_data: dict) -> Result:
        query = (
            update(self.model)
            .where(self.model.id == uuid_)
            .values(**new_data)
            .returning(self.model)
        )

        res = self.session.execute(statement=query)

        return res.scalar_one()

    def delete_instance(self, uuid_: uuid.UUID) -> Result:
        query = (
            delete(self.model)
            .where(self.model.id == uuid_)
            .returning(self.model)
        )

        res = self.session.execute(statement=query)

        return res.scalar_one()
