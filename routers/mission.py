import uuid

from fastapi import APIRouter, Depends

from dependencies import (
    get_mission_service,
    get_target_service,
)
from schemas.mission import (
    MissionCreateSchema,
    MissionListSchema,
    MissionReadSchema,
)
from schemas.target import TargetUpdateSchema
from services.mission import MissionService
from services.target import TargetService

missions_router = APIRouter(prefix="/missions", tags=["missions"])


@missions_router.post("/create_mission/", response_model=MissionReadSchema)
def create_mission(
    mission_data: MissionCreateSchema,
    service: MissionService = Depends(get_mission_service),
):
    return service.create_mission(mission_data=mission_data)


@missions_router.get("/all_missions/", response_model=MissionListSchema)
def get_all_missions(service: MissionService = Depends(get_mission_service)):
    missions = service.list_all_mission()
    return MissionListSchema(
        missions=[
            MissionReadSchema(**mission.__dict__) for mission in missions
        ]
    )


@missions_router.get("/{uuid_}/", response_model=MissionReadSchema)
def get_mission_by_id(
    mission_uuid: uuid.UUID,
    service: MissionService = Depends(get_mission_service),
):
    return service.get_mission_by_uuid(mission_uuid=mission_uuid)


@missions_router.patch(
    "/{mission_uuid}/assign/{cat_uuid}", response_model=MissionReadSchema
)
def assign_cat_to_mission(
    mission_uuid: uuid.UUID,
    cat_uuid: uuid.UUID,
    service: MissionService = Depends(get_mission_service),
):
    return service.assign_cat_to_mission(
        mission_uuid=mission_uuid, cat_uuid=cat_uuid
    )


@missions_router.patch("/{mission_uuid}/", response_model=MissionReadSchema)
def mark_as_completed(
    mission_uuid: uuid.UUID,
    service: MissionService = Depends(get_mission_service),
):
    return service.mark_as_completed(mission_uuid=mission_uuid)


@missions_router.patch(
    "/{mission_uuid}/target/{target_uuid}/complete",
    response_model=MissionReadSchema,
)
def mark_target_as_completed(
    mission_uuid: uuid.UUID,
    target_uuid: uuid.UUID,
    target_service: TargetService = Depends(get_target_service),
    mission_service: MissionService = Depends(get_mission_service),
):
    mission_service.get_mission_by_uuid(
        mission_uuid=mission_uuid
    )  # just check that mission exists
    target_service.mark_target_as_completed(target_uuid=target_uuid)
    return mission_service.get_mission_by_uuid(mission_uuid=mission_uuid)


@missions_router.patch(
    "/{mission_uuid}/target/{target_uuid}/update_notes",
    response_model=MissionReadSchema,
)
def update_notes_of_target(
    mission_uuid: uuid.UUID,
    target_uuid: uuid.UUID,
    notes: TargetUpdateSchema,
    target_service: TargetService = Depends(get_target_service),
    mission_service: MissionService = Depends(get_mission_service),
):
    mission_service.get_mission_by_uuid(
        mission_uuid=mission_uuid
    )  # just check that mission exists
    target_service.update_notes(target_uuid=target_uuid, notes=notes)
    return mission_service.get_mission_by_uuid(mission_uuid=mission_uuid)


@missions_router.delete(
    "/{mission_uuid}/delete", response_model=MissionReadSchema
)
def delete_mission(
    mission_uuid: uuid.UUID,
    service: MissionService = Depends(get_mission_service),
):
    return service.delete_mission(mission_uuid=mission_uuid)
