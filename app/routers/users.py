from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.libs.utils.classes import User
from app.libs.config.users import get_users, add_user, get_characters, remove_user

router = APIRouter(
    prefix="/user"
)


@router.get("/", tags=["Users"])
def get_users_all():
    return get_users()


@router.post("/", tags=["Users"], status_code=201)
def post_user(user: User):
    res, code = add_user(user)
    if code != 201:
        raise HTTPException(status_code=code, detail=res['value'])
    return res


@router.get("/characters", tags=["Users"])
def get_character_list():
    return get_characters()


@router.delete("/{name}", tags=["Users"])
def delete_user(name: str):
    return remove_user(name)
