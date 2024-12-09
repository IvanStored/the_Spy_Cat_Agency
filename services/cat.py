import http
import uuid

import requests
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound

from repos.cat import CatRepo


class CatService:
    def __init__(self, cat_repo: CatRepo):
        self.repo = cat_repo
        self.__get_breeds()

    def __check_existing(self, uuid_):
        try:
            return self.repo.get_by_uuid(uuid_=uuid_)
        except NoResultFound:
            raise HTTPException(
                status_code=http.HTTPStatus.NOT_FOUND,
                detail=f"Cat {uuid_} was not found",
            )

    def __get_breeds(self):
        resp = requests.get("https://api.thecatapi.com/v1/breeds")
        self.breeds = [cat["name"] for cat in resp.json()]

    def create_cat(self, cat_data: dict):
        if cat_data["breed"] not in self.breeds:
            raise HTTPException(
                status_code=http.HTTPStatus.BAD_REQUEST,
                detail="Breed not exists at CatsAPI",
            )
        return self.repo.create_instance(cat_data)

    def get_cat_by_uuid(self, cat_uuid: uuid.UUID):
        return self.__check_existing(uuid_=cat_uuid)

    def delete_cat(self, cat_uuid: uuid.UUID):
        self.__check_existing(uuid_=cat_uuid)
        return self.repo.delete_instance(uuid_=cat_uuid)

    def update_cat(self, cat_uuid: uuid.UUID, new_data: dict):
        return self.repo.update_instance(uuid_=cat_uuid, new_data=new_data)

    def list_all_cats(self):
        return self.repo.list()
