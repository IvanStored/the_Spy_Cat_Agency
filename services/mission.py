import http
import uuid
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError

from models.mission import Mission
from repos.mission import MissionRepo
from models.target import Target
from schemas.mission import MissionCreateSchema


class MissionService:

    def __init__(self, mission_repo: MissionRepo):
        self.repo = mission_repo

    def __check_existing(self, uuid_):
        try:
            return self.repo.get_by_uuid(uuid_=uuid_)
        except NoResultFound:
            raise HTTPException(
                status_code=http.HTTPStatus.NOT_FOUND,
                detail=f"Mission {uuid_} was not found",
            )

    def create_mission(self, mission_data: MissionCreateSchema):

        if len(mission_data.targets) > 3:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Mission can have only 3 targets",
            )
        try:
            mission = self.repo.create_instance(
                instance_data=mission_data.model_dump(exclude={"targets"})
            )
        except IntegrityError:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="This cat already have a mission",
            )
        targets = [
            Target(
                mission_id=mission.id,
                name=target.name,
                country=target.country,
                notes=target.notes,
            )
            for target in mission_data.targets
        ]

        mission.targets.extend(targets)
        self.repo.session.add(mission)
        self.repo.session.commit()
        return self.repo.get_by_uuid(uuid_=mission.id)

    def list_all_mission(self):
        return self.repo.list()

    def get_mission_by_uuid(self, mission_uuid: uuid.UUID):
        mission = self.__check_existing(uuid_=mission_uuid)
        if all(target.complete for target in mission.targets):
            self.mark_as_completed(mission_uuid)
        return self.__check_existing(uuid_=mission_uuid)

    def assign_cat_to_mission(
        self, mission_uuid: uuid.UUID, cat_uuid: uuid.UUID
    ):
        mission = self.get_mission_by_uuid(mission_uuid=mission_uuid)
        if mission.is_completed:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Mission is already completed",
            )
        if mission.cat_uuid:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Mission is already assigned to cat",
            )
        try:
            mission.cat_uuid = cat_uuid
        except IntegrityError:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Cat already have a mission",
            )
        return self.get_mission_by_uuid(mission_uuid=mission_uuid)

    def delete_mission(self, mission_uuid: uuid.UUID):
        mission = self.get_mission_by_uuid(mission_uuid=mission_uuid)
        if mission.cat_uuid:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Mission is already assigned to cat, cant be deleted",
            )
        return self.repo.delete_instance(uuid_=mission_uuid)

    def mark_as_completed(self, mission_uuid: uuid.UUID):
        mission = self.__check_existing(uuid_=mission_uuid)
        if mission.is_completed:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Mission is already completed",
            )
        mission.is_completed = True
        return mission
