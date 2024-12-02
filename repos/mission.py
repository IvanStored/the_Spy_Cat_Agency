from models.mission import Mission
from repos.base import BaseRepo


class MissionRepo(BaseRepo):
    model = Mission
