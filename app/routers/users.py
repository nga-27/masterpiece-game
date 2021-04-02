from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.libs.utils.classes import User, NewPosition
from app.libs.config.users import (
    get_users, add_user, get_characters, remove_user, user_move_piece,
    pick_starting_position
)

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


@router.delete("/{name}", tags=["Users"], status_code=201)
def delete_user(name: str):
    res, code = remove_user(name)
    if code != 201:
        raise HTTPException(status_code=code, detail=res['value'])
    return res


#####################################

@router.get("/characters", tags=["Users"])
def get_character_list():
    return get_characters()


#####################################


@router.patch("/update_position", tags=["Users"], status_code=201)
def update_user_position(new_position: NewPosition):
    name = new_position.name
    roll = new_position.roll_value
    direction = new_position.move_direction
    if roll and direction and name:
        res, code = user_move_piece(name, roll, direction)
        if code != 201:
            raise HTTPException(status_code=code, detail=res['value'])
        return res
    raise HTTPException(status_code=400, detail={
                        "value": "Badly formed patch."})


@router.patch("/start_position", tags=["Users"], status_code=201)
def add_user_starter_position(new_position: NewPosition):
    name = new_position.name
    position = new_position.position
    if (position >= 0) and name:
        res, code = pick_starting_position(name, position)
        if code != 201:
            raise HTTPException(status_code=code, detail=res['value'])
        return res
    raise HTTPException(status_code=400, detail={
                        "value": "Badly formed start position."})
