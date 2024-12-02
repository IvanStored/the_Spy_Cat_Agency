import http
import uuid

from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound

from repos.target import TargetRepo


class TargetService:

    def __init__(self, target_repo: TargetRepo):
        self.repo = target_repo

    def __check_existing(self, uuid_):
        try:
            return self.repo.get_by_uuid(uuid_=uuid_)
        except NoResultFound:
            raise HTTPException(
                status_code=http.HTTPStatus.NOT_FOUND,
                detail=f"Target {uuid_} was not found",
            )

    def get_target_by_uuid(self, target_uuid: uuid.UUID):
        return self.__check_existing(uuid_=target_uuid)

    def mark_target_as_completed(self, target_uuid: uuid.UUID):
        target = self.get_target_by_uuid(target_uuid=target_uuid)
        if target.complete:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Target is already completed",
            )
        target.complete = True

    def update_notes(self, target_uuid, notes: dict):
        target = self.get_target_by_uuid(target_uuid=target_uuid)
        if target.complete or target.mission.is_completed:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Target or mission is already completed, you can`t update notes",
            )
        return self.repo.update_instance(uuid_=target_uuid, new_data=notes)
