from fastapi import Depends

from database.db import get_sync_session
from repos.cat import CatRepo
from repos.mission import MissionRepo
from repos.target import TargetRepo
from services.cat import CatService
from services.mission import MissionService
from services.target import TargetService


def get_cat_service(session=Depends(get_sync_session)):
    repo = CatRepo(session=session)
    return CatService(cat_repo=repo)


def get_mission_service(session=Depends(get_sync_session)):
    repo = MissionRepo(session=session)
    return MissionService(mission_repo=repo)


def get_target_service(session=Depends(get_sync_session)):
    repo = TargetRepo(session=session)
    return TargetService(target_repo=repo)
