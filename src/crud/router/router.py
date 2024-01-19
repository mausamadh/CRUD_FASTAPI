from fastapi import APIRouter,status
from src.crud.service.service import service
crud=APIRouter(prefix="/api/v1/crud",tags=["CRUD"])



@crud.get("/get",status_code=status.HTTP_200_OK)
async def crud_get(index:int):
    return service().get(index=index)

@crud.get("/add",status_code=status.HTTP_200_OK)
async def crud_get(data:int):
    return service().add(data=data)


@crud.get("/update",status_code=status.HTTP_200_OK)
async def crud_get(index:int,data:int):
    return service().update(index=index,data=data)


@crud.get("/delete",status_code=status.HTTP_200_OK)
async def crud_get(index:int):
    return service().delete(index=index)