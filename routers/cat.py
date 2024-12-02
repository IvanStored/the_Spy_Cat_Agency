import uuid

from fastapi import APIRouter, Depends

from dependencies import get_cat_service
from schemas.cat import (
    CatCreateSchema,
    CatReadSchema,
    CatUpdateSchema,
    CatListSchema,
)
from services.cat import CatService

cats_router = APIRouter(prefix="/cats", tags=["cats"])


@cats_router.post("/create_cat", response_model=CatReadSchema)
async def create_cat(
    cat_data: CatCreateSchema, service: CatService = Depends(get_cat_service)
):
    return service.create_cat(cat_data=cat_data.__dict__)


@cats_router.get("/all_cats", response_model=CatListSchema)
async def list_all_cats(service: CatService = Depends(get_cat_service)):
    cats = service.list_all_cats()
    return CatListSchema(cats=[CatReadSchema(**cat.__dict__) for cat in cats])


@cats_router.get("/{uuid_}/", response_model=CatReadSchema)
async def get_cat_by_uuid(
    cat_uuid: uuid.UUID, service: CatService = Depends(get_cat_service)
):
    return service.get_cat_by_uuid(cat_uuid=cat_uuid)


@cats_router.patch("/update_salary/{uuid_}", response_model=CatReadSchema)
async def update_info(
    cat_uuid: uuid.UUID,
    new_data: CatUpdateSchema,
    service: CatService = Depends(get_cat_service),
):
    return service.update_cat(
        cat_uuid=cat_uuid, new_data=new_data.model_dump(exclude_none=True)
    )


@cats_router.delete("/delete_cat/{uuid_}", response_model=CatReadSchema)
async def delete_cat(
    cat_uuid: uuid.UUID, service: CatService = Depends(get_cat_service)
):
    return service.delete_cat(cat_uuid=cat_uuid)
