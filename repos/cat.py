from models.cat import Cat
from repos.base import BaseRepo


class CatRepo(BaseRepo):
    model = Cat
